from flask import Blueprint, request, jsonify

#user_bp = Blueprint('users', __name__)
#Addition
user_bp = Blueprint('users', __name__, url_prefix='/api/users')

#Addition
USERS = {
    1: {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
    2: {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
}
NEXT_USER_ID = 3

#Addition
@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify(list(USERS.values()))


# @user_bp.route('/', methods=['GET'])
# def get_users():
#     return jsonify([
#         {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
#         {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
#     ])

#Addition
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in USERS:
        return jsonify(USERS[user_id])
    return jsonify({'error': 'User not found'}), 404



# @user_bp.route('/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     users = {
#         1: {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
#         2: {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
#     }
    
#     if user_id in users:
#         return jsonify(users[user_id])
#     return jsonify({'error': 'User not found'}), 404


#Addition
@user_bp.route('/', methods=['POST'])
def create_user():
    global NEXT_USER_ID

    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400

    new_user = {'id': NEXT_USER_ID, 'name': data['name'], 'email': data['email']}
    USERS[NEXT_USER_ID] = new_user
    NEXT_USER_ID += 1

    return jsonify(new_user), 201



# @user_bp.route('/', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     if not data or 'name' not in data or 'email' not in data:
#         return jsonify({'error': 'Name and email are required'}), 400
    
#     return jsonify({'id': 3, 'name': data['name'], 'email': data['email']}), 201