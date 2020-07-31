from flask import Flask
from bmc.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

bmc_app = Flask(__name__)
bmc_app.config.from_object(Config)
db = SQLAlchemy(bmc_app)
migrate = Migrate(bmc_app, db)
login = LoginManager(bmc_app)
login.login_view = 'login'

from bmc import routes, models, errors
