from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir llamadas desde el frontend

@app.route('/')
def home():
    return jsonify({"message": "Hola desde el backend Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
