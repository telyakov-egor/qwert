from flask import Flask, request, jsonify

app = Flask(__name__)

# Данные о продажах продуктов будут храниться в памяти
sales = []

# Уникальный идентификатор для каждой записи
next_id = 1

@app.route('/sales', methods=['GET'])
def get_sales():
    sort_by = request.args.get('sort_by')
    order = request.args.get('order', 'asc')
    sorted_sales = sorted(sales, key=lambda x: x.get(sort_by, 0), reverse=(order == 'desc')) if sort_by else sales
    return jsonify(sorted_sales)

@app.route('/sales', methods=['POST'])
def add_sale():
    global next_id
    new_sale = request.json
    new_sale['id'] = next_id
    next_id += 1
    sales.append(new_sale)
    return jsonify({'status': 'Sale added successfully'}), 201

@app.route('/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    update_data = request.json
    for sale in sales:
        if sale['id'] == sale_id:
            sale.update(update_data)
            return jsonify({'status': 'Sale updated successfully'})
    return jsonify({'status': 'Sale not found'}), 404

@app.route('/sales/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    global sales
    sales = [sale for sale in sales if sale['id'] != sale_id]
    return jsonify({'status': 'Sale deleted successfully'})

@app.route('/sales/stats', methods=['GET'])
def get_stats():
    if not sales:
        return jsonify({'average_price': None, 'max_price': None, 'min_price': None, 'average_quantity_sold': None, 'max_quantity_sold': None, 'min_quantity_sold': None})
    prices = [sale['price'] for sale in sales]
    quantities = [sale['quantity_sold'] for sale in sales]
    return jsonify({
        'average_price': sum(prices) / len(prices),
        'max_price': max(prices),
        'min_price': min(prices),
        'average_quantity_sold': sum(quantities) / len(quantities),
        'max_quantity_sold': max(quantities),
        'min_quantity_sold': min(quantities)
    })

if __name__ == '__main__':
    app.run(debug=True)
