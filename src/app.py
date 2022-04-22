import os
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request
from models import db, ma
from flask_migrate import Migrate
from controllers.authenticate_user_controller import authentication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['GITHUB_CLIENT_ID'] = os.getenv('GITHUB_CLIENT_ID')
app.config['GITHUB_CLIENT_SECRET'] = os.getenv('GITHUB_CLIENT_SECRET')
load_dotenv()
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')

@app.route('/')
def root():
    return {'message': 'Server is running'}

@app.route('/github')
def github():
    return redirect(f'https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}')

@app.route('/login/callback')
def callback():
    args = request.args
    code = args['code']
    
    return jsonify(code)

app.register_blueprint(authentication, url_prefix='/api/v1')