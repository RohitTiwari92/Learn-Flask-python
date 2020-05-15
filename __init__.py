from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:////DB/userresttest.db'
db = SQLAlchemy(app)
api=Api(app)
