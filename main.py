from flask import Flask, request, jsonify
from urllib.parse import quote  # Измененный импорт

app = Flask(__name__)

sales = []

@app.route('/sales', methods=['GET'])
def get_sales():
    return jsonify(sales), 200

@app.route('/sales', methods=['POST'])
def add_sale():
    sale = request.get_json()
    sales.append(sale)
    return jsonify(sale), 201

@app.route('/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    sale = request.get_json()
    sales[sale_id] = sale
    return jsonify(sale), 200

@app.route('/sales/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    sales.pop(sale_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
