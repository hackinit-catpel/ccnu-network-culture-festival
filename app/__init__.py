# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import redis
#from flask.ext.redis import FlaskRedis
#from flask_debugtoolbar import DebugToolbarExtension
from config import config


app = Flask(__name__)
"""
config
 -- 'default': DevelopmentConfig
 -- 'develop': DevelopmentConfig
 -- 'testing': TestingConfig
 -- 'production': ProductionConfig
    you can edit this in config.py
"""
config_name = 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)
#toolbar = DebugToolbarExtension(app)


# Redis Config
r1 = redis.StrictRedis(host='localhost', port=6379, db=0)


db = SQLAlchemy(app)
login_manager = LoginManager(app)
#redis_store = FlaskRedis(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


# admin site
from admin import views


"""
blueprint
you can register a <blueprint> by run:
 -- mana blueprint <blueprint>
under app folder
"""
from main import main
app.register_blueprint(main, url_prefix='/main')

from auth import auth
app.register_blueprint(auth, url_prefix="/auth")

from admin import admin
app.register_blueprint(admin,url_prefix="/admin")

from admin_api_1_0 import admin_api
app.register_blueprint(admin_api,url_prefix="/admin/api")
