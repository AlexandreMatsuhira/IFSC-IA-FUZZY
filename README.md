# Sistema de Controle de Semáforos Inteligente com Lógica Fuzzy

**Trabalho da disciplina de Inteligência Artificial**  
**Professor: Wilson Castello**  

## 📝 Descrição do Projeto

Este projeto implementa um sistema inteligente de controle de semáforos utilizando Lógica Fuzzy para otimizar o fluxo de veículos em uma avenida de 2000m com 4 semáforos equidistantes. O sistema adapta dinamicamente os tempos dos semáforos com base em quatro variáveis principais:

- 🚗 Densidade de veículos em cada segmento
- 🚦 Velocidade média dos veículos
- ⏳ Tempo de espera nos semáforos
- 🚧 Ocorrência de incidentes (acidentes, obras)

## 🛠️ Tecnologias Utilizadas

- <img src="https://img.icons8.com/color/48/000000/python.png" width="16"/> Python 3.x
- <img src="https://img.icons8.com/ios/50/000000/flask.png" width="16"/> Flask (framework web)
- 📊 Skfuzzy (biblioteca para lógica fuzzy)
- 📈 Chart.js (visualização de dados)
- 🌐 HTML/CSS/JavaScript (interface web)

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. Python 3.x instalado
2. Gerenciador de pacotes pip

### Passo a Passo para Inicialização

1. **Clone o repositório ou baixe os arquivos**

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o servidor:**

```bash
python src/app.py
```

4. **Acesse a aplicação no navegador:**

Abra [http://localhost:5000](http://localhost:5000) no seu navegador preferido


## ✨ Funcionalidades Principais

1. **Monitoramento em tempo real** dos 4 segmentos da avenida
2. **Cálculo inteligente** dos tempos dos semáforos usando lógica fuzzy
3. **Visualização gráfica** interativa dos dados de tráfego
4. **Atualização automática** dos dados (a cada 5 segundos)
5. **Simulação visual** realista dos estados dos semáforos

## 📊 Dados Técnicos do Projeto

| Característica          | Detalhe                          |
|-------------------------|----------------------------------|
| Comprimento da avenida  | 2000 metros                     |
| Número de semáforos     | 4 (posicionados a cada 500m)    |
| Variáveis de entrada    | Densidade (0-100%), Velocidade (0-80 km/h), Espera (0-300s), Incidentes (0-5) |
| Variável de saída       | Tempo do sinal verde (10-120s)  |

## 📚 Observações Importantes

- Este projeto utiliza dados simulados para demonstração
- Desenvolvido como trabalho acadêmico para a disciplina de Inteligência Artificial
- Pode ser utilizado como base para outros trabalhos acadêmicos

## 📜 Licença

Este projeto é para fins educacionais e pode ser utilizado como referência, desde que citada a fonte.