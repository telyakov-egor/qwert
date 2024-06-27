import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_sales(client):
    rv = client.get('/sales')
    assert rv.status_code == 200

def test_add_sale(client):
    rv = client.post('/sales', json={
        'product_name': 'Banana',
        'category': 'Fruit',
        'price': 1.0,
        'quantity_sold': 5,
        'sale_date': '2024-06-27'
    })
    assert rv.status_code == 201
