from flask import Flask
from config import Config
from init_db import db

from views.department import department
from views.employee import employee
from views.home import home

app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = "Secret Key"

db.init_app(app)


def create_app():
    app.register_blueprint(department)
    app.register_blueprint(employee)
    app.register_blueprint(home)

    return app
