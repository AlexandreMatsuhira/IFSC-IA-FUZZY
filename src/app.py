from flask import Flask, render_template, request, jsonify
from fuzzy_logic import FuzzyTrafficController
import random

app = Flask(__name__)

# Inicializa o controlador fuzzy
fuzzy_controller = FuzzyTrafficController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_traffic_data')
def get_traffic_data():
    # Simula dados de sensores (em um sistema real, isso viria de sensores reais)
    segments = []
    for i in range(4):
        segments.append({
            'id': i+1,
            'density': random.randint(0, 100),
            'avg_speed': random.randint(0, 80),
            'wait_time': random.randint(0, 300),
            'incidents': random.randint(0, 5)
        })
    print(segments)
    
    # Processa os dados com lógica fuzzy
    traffic_lights = fuzzy_controller.calculate_light_times(segments)
    
    return jsonify({
        'segments': segments,
        'traffic_lights': traffic_lights
    })

@app.route('/update_lights', methods=['POST'])
def update_lights():
    data = request.json
    print(request)
    segments = data['segments']
    
    # Processa os dados com lógica fuzzy
    traffic_lights = fuzzy_controller.calculate_light_times(segments)
    
    return jsonify({
        'traffic_lights': traffic_lights
    })

if __name__ == '__main__':
    app.run(debug=True)