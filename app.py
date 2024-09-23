from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Dados simulados
    data = [
        {"id": 1, "name": "item1", "value": 100},
        {"id": 2, "name": "item2", "value": 150},
        {"id": 3, "name": "item3", "value": 200}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
