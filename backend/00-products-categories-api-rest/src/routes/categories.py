from flask import Blueprint

categories_bp = Blueprint('/', __name__, template_folder='routes')

@categories_bp.route('/api/categories', methods=['GET'])
def read():
    return '<p>Get All</p>'

@categories_bp.route('/api/categories/<int:categoryId>', methods=['GET'])
def readOne(categoryId):
    return f'<p>Get One { categoryId }</p>'

@categories_bp.route('/api/categories', methods=['POST'])
def create():
    return '<p>Create</p>'

@categories_bp.route('/api/categories/<int:categoryId>', methods=['PUT'])
def update(categoryId):
    return f'<p>Update One { categoryId }</p>'

@categories_bp.route('/api/categories/<int:categoryId>', methods=['DELETE'])
def delete(categoryId):
    return f'<p>Delete One { categoryId }</p>'