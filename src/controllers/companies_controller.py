from flask import Blueprint, jsonify, request
from services.companies_service import CompaniesService

companies = Blueprint('companies', __name__)

@companies.route('/companies', methods=['POST'])
def create_company():
    try:
        companiesService = CompaniesService()
        data = request.json

        company = companiesService.create_company(data)
        return jsonify(company), 201
    except Exception as err:
        return jsonify({'message': str(err)}), 400