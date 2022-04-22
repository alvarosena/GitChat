import os
from flask import Flask
from models import db, ma

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
ma.init_app(app)

@app.route('/')
def root():
    return {'message': 'Server is running'}
