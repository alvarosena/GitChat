from flask import Blueprint, jsonify, request

from services.authenticate_user_service import AuthenticateUserService

authentication = Blueprint('authentication', __name__)

@authentication.route('/authenticate', methods=['POST'])
def authenticate_user():
    try:
        authenticateUserService = AuthenticateUserService()

        data = request.json

        result = authenticateUserService.authenticate(data)
        return jsonify(result), 201 
    except Exception as err:
        return jsonify({'message': str(err)}), 400
