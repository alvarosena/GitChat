import os

import requests

class AuthenticateUserService:
    def authenticate(self, data):
        params = {
            'client_id': os.getenv('GITHUB_CLIENT_ID'),
            'client_secret': os.getenv('GITHUB_CLIENT_SECRET'),
            'code': data['code']
        }
        headers = {
            'Accept': 'application/json',
        }

        response = requests.post('https://github.com/login/oauth/access_token', params=params, headers=headers)
        data = response.json()
        return data