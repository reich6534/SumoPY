from flask import Flask
from bmc.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bmc_app = Flask(__name__)
bmc_app.config.from_object(Config)
db = SQLAlchemy(bmc_app)
migrate = Migrate(bmc_app, db)

from bmc import routes, models
