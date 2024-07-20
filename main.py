from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Bienvenido a la API de Predicción</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Simulación de predicción: suma de dos números
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        resultado = num1 + num2
        return jsonify({'resultado': resultado})
    return jsonify({'error': 'Datos inválidos'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
