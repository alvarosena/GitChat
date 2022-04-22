import os
import requests
from models import db, Employer, employer_schema

class AuthenticateUserService:
    def authenticate(self, data):
        response = requests.post('https://github.com/login/oauth/access_token', 
            params = {
                'client_id': os.getenv('GITHUB_CLIENT_ID'),
                'client_secret': os.getenv('GITHUB_CLIENT_SECRET'),
                'code': data['code']
            },
            headers = {
                'Accept': 'application/json',
            }
        )

        data = response.json()
        access_token = data['access_token']

        user = requests.get('https://api.github.com/user', 
            headers = {
                'Accept': 'application/json',
                'authorization': f'Bearer {access_token}'
            }
        
        )
        data = user.json()

        employer_exists = Employer.query.filter_by(github_id=data['id']).first()

        if employer_exists:
            raise Exception("Employer already exists")
        else:
            employer = Employer(name=data['name'], avatar_url=data['avatar_url'], github_id=data['id'])
            db.session.add(employer)
            db.session.commit()

            return employer_schema.dump(employer)
    

