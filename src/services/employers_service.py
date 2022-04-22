from models import db, Employer, employers_schema

class EmployersService:
    def list_employers(self):
        employers = Employer.query.all()
        return employers_schema.dump(employers)