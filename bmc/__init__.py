from bmc.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from google.cloud import speech_v1p1beta1

bmc_app = Flask(__name__)
bmc_app.config.from_object(Config)
db = SQLAlchemy(bmc_app)
migrate = Migrate(bmc_app, db)
login = LoginManager(bmc_app)
login.login_view = 'login'
bootstrap = Bootstrap(bmc_app)
bmc_app.speech_client = speech_v1p1beta1.SpeechClient.from_service_account_json("./private/sumopy.json")

from bmc import routes, models, errors

if (not bmc_app.debug):
    if (bmc_app.config['MAIL_SERVER']):
        auth = None
        if (bmc_app.config['MAIL_USERNAME'] or bmc_app.config['MAIL_PASSWORD']):
            auth = (bmc_app.config['MAIL_USERNAME'], bmc_app.config['MAIL_PASSWORD'])
        secure = None
        if (bmc_app.config['MAIL_USE_TLS']):
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(bmc_app.config['MAIL_SERVER'], bmc_app.config['MAIL_PORT']),
            fromaddr='no-reply@' + bmc_app.config['MAIL_SERVER'],
            toaddrs=bmc_app.config['ADMINS'], subject='Website failure',
            credentials=auth, secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        bmc_app.logger.addHandler(mail_handler)

    if (not os.path.exists('logs')):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/website.log', maxBytes=10240, 
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d'
    ))
    file_handler.setLevel(logging.INFO)
    bmc_app.logger.addHandler(file_handler)

    bmc_app.logger.setLevel(logging.INFO)
    bmc_app.logger.info('Website startup')
    