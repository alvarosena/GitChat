from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from services.employers_service import EmployersService

employers = Blueprint('employers', __name__)

@employers.route('/employers')
def list_employers():
    employersService = EmployersService()

    employers = employersService.list_employers()
    return jsonify(employers)

@employers.route('/employers', methods=['PUT'])
@jwt_required()
def create_work():
    try:
        employersService = EmployersService()

        data = request.json
        employer_id = get_jwt_identity()

        employer = employersService.create_work(data, employer_id)
        return jsonify(employer)
    except Exception as err:
        return jsonify({'error': str(err)}), 404
