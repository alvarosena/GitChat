from models import db, Employer, employers_schema, employer_schema

class EmployersService:
    def list_employers(self):
        employers = Employer.query.all()
        return employers_schema.dump(employers)

    def create_work(self, data, employer_id):
        employer = Employer.query.filter_by(id=employer_id).first()

        if not employer:
            raise Exception("Employer does not exists.")

        employer.work_as = data['work_as']        
        db.session.commit()

        return employer_schema.dump(employer)
