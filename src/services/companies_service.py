from models import db, Company, companies_schema, company_schema

class CompaniesService:
    def create_company(self, data):
        company_exists = Company.query.filter_by(name=data['name']).first()

        if company_exists:
            raise Exception("Company already exists.")

        company = Company(name=data['name'], avatar_url=data['avatar_url'])
        db.session.add(company)
        db.session.commit()
        
        return company_schema.dump(company)