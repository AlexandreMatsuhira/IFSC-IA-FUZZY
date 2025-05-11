# Semáforo Fuzzy

Este projeto simula o controle inteligente de semáforos em uma avenida usando lógica fuzzy, considerando densidade de veículos, velocidade média, tempo de espera e incidentes em cada segmento.

## Como rodar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o servidor:

```bash
python src/app.py
```

3. Acesse a interface web em [http://localhost:5000](http://localhost:5000)

## Como funciona

- Preencha os dados dos sensores para cada segmento da avenida.
- O sistema calcula o tempo ideal de abertura para cada semáforo usando lógica fuzzy.
- Os tempos sugeridos são exibidos na tela.

## Estrutura
- `src/app.py`: servidor Flask e interface web
- `src/fuzzy_logic.py`: lógica fuzzy para cálculo dos tempos
- `templates/index.html`: interface web