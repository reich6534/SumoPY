from flask import Flask
from bmc.config import Config

bmc_app = Flask(__name__)
bmc_app.config.from_object(Config)

from bmc import routes
