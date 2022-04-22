import os
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request
from models import db, ma
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from routes.routes import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY') 
app.config['GITHUB_CLIENT_ID'] = os.getenv('GITHUB_CLIENT_ID')
app.config['GITHUB_CLIENT_SECRET'] = os.getenv('GITHUB_CLIENT_SECRET')
load_dotenv()
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

routes(app)

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