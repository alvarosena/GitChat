import os
import requests

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
        return data
    

