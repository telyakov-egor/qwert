from flask_restx import fields

def create_product_model(api):
    return api.model('Product', {
        'id': fields.Integer(readonly=True, description='The product unique identifier'),
        'name': fields.String(required=True, description='The product name'),
        'price': fields.Float(required=True, description='The product price'),
        'quantity': fields.Integer(required=True, description='The product quantity'),
        'category': fields.String(required=True, description='The product category')
    })
