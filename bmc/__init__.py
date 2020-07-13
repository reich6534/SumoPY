from flask import Flask

bmc_app = Flask(__name__)

from bmc import routes
