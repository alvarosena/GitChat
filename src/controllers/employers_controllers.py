from flask import Blueprint, jsonify
from services.employers_service import EmployersService

employers = Blueprint('employers', __name__)

@employers.route('/employers')
def list_employers():
    employersService = EmployersService()

    employers = employersService.list_employers()
    return jsonify(employers)