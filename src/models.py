from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql import func
from utils.generate_uuid import Uuid

db = SQLAlchemy()
ma = Marshmallow()

class Employer(db.Model):
    __tablename__ = 'employers'

    id = db.Column(db.String, primary_key=True, default=Uuid.generate())
    name = db.Column(db.String, nullable=False)
    avatar_url = db.Column(db.String, nullable=False)
    github_id = db.Column(db.String, nullable=False)
    work_as = db.Column(db.String, nullable=True)
    company_id = db.Column(db.String, db.ForeignKey('companies.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())


class EmployerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "avatar_url", "github_id", "work_as", "created_at")

employer_schema = EmployerSchema()
employers_schema = EmployerSchema(many=True)

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.String, primary_key=True, default=Uuid.generate())
    name = db.Column(db.String, nullable=False)
    avatar_url = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    employers = db.relationship('Employer')

class CompanySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "avatar_url", "created_at")

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)
