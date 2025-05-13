import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyTrafficController:
    def __init__(self):
        # Variáveis de entrada
        self.density = ctrl.Antecedent(np.arange(0, 101, 1), 'density')
        self.avg_speed = ctrl.Antecedent(np.arange(0, 81, 1), 'avg_speed')
        self.wait_time = ctrl.Antecedent(np.arange(0, 301, 1), 'wait_time')
        self.incidents = ctrl.Antecedent(np.arange(0, 6, 1), 'incidents')
        
        # Variável de saída
        self.green_time = ctrl.Consequent(np.arange(0, 121, 1), 'green_time')
        
        # Funções de pertinência para as variáveis de entrada
        self._setup_membership_functions()
        
        # Regras fuzzy
        self._setup_rules()
        
        # Sistema de controle
        self.traffic_ctrl = ctrl.ControlSystem(self.rules)
        self.traffic_sim = ctrl.ControlSystemSimulation(self.traffic_ctrl)
    
    def _setup_membership_functions(self):
        # Densidade de veículos (0-100%)
        self.density['low'] = fuzz.zmf(self.density.universe, 20, 50) 
        self.density['medium'] = fuzz.trapmf(self.density.universe, [30, 40, 60, 70])
        self.density['high'] = fuzz.smf(self.density.universe, 55, 80) 
        
        # Velocidade média (0-80 km/h)
        self.avg_speed['low'] = fuzz.zmf(self.avg_speed.universe, 20, 40)
        self.avg_speed['medium'] = fuzz.gaussmf(self.avg_speed.universe, 50, 10)
        self.avg_speed['high'] = fuzz.smf(self.avg_speed.universe, 40, 60)
        
        # Tempo de espera (0-300 segundos)
        self.wait_time['low'] = fuzz.zmf(self.wait_time.universe, 30, 90)
        self.wait_time['medium'] = fuzz.trapmf(self.wait_time.universe, [60, 90, 150, 180])
        self.wait_time['high'] = fuzz.smf(self.wait_time.universe, 120, 180)
        
        # Incidentes (0-5)
        self.incidents['low'] = fuzz.zmf(self.incidents.universe, 1, 2)
        self.incidents['medium'] = fuzz.trapmf(self.incidents.universe, [1, 2, 3, 4])
        self.incidents['high'] = fuzz.smf(self.incidents.universe, 3, 4)
        
        # Tempo do sinal verde (0-120 segundos)
        self.green_time['short'] = fuzz.zmf(self.green_time.universe, 20, 40)
        self.green_time['medium'] = fuzz.trapmf(self.green_time.universe, [30, 50, 70, 90])
        self.green_time['long'] = fuzz.smf(self.green_time.universe, 60, 90)
    
    def _setup_rules(self):
        self.rules = [
            # Regras de segurança (incidentes primeiro)
            ctrl.Rule(self.incidents['high'], self.green_time['short']),  # Prioridade máxima
            ctrl.Rule(self.incidents['medium'], self.green_time['medium']),

            # Regras para alta densidade
            ctrl.Rule(
                self.density['high'] & self.wait_time['high'] & self.avg_speed['low'], 
                self.green_time['long']
            ),
            ctrl.Rule(
                self.density['high'] & self.wait_time['medium'], 
                self.green_time['medium']
            ),

            # Regras para média densidade
            ctrl.Rule(
                self.density['medium'] & self.avg_speed['medium'], 
                self.green_time['medium']
            ),
            ctrl.Rule(
                self.density['medium'] & self.wait_time['low'], 
                self.green_time['short']
            ),

            # Regras para baixa densidade
            ctrl.Rule(
                self.density['low'] & self.avg_speed['high'], 
                self.green_time['short']
            ),
            ctrl.Rule(
                self.density['low'] & self.wait_time['low'], 
                self.green_time['short']
            ),

            # Regras de fallback (casos não cobertos)
            ctrl.Rule(
                self.wait_time['high'] | self.avg_speed['low'], 
                self.green_time['long']
            ),
            ctrl.Rule(
                ~self.density['high'] & ~self.wait_time['high'], 
                self.green_time['medium']
            )
        ]
    
    def calculate_light_times(self, segments):
        light_times = []
        
        for segment in segments:
            # Configura as entradas do sistema fuzzy
            self.traffic_sim.input['density'] = segment['density']
            self.traffic_sim.input['avg_speed'] = segment['avg_speed']
            self.traffic_sim.input['wait_time'] = segment['wait_time']
            self.traffic_sim.input['incidents'] = segment['incidents']
            
            # Computa o sistema
            self.traffic_sim.compute()
            
            # Obtém o tempo do sinal verde
            green_time = self.traffic_sim.output['green_time']
            
            # Garante que o tempo esteja dentro dos limites
            green_time = max(10, min(120, green_time))
            
            light_times.append({
                'id': segment['id'],
                'green_time': round(green_time),
                'red_time': round(green_time * 1.5)  # Tempo vermelho proporcional
            })
        
        return light_times