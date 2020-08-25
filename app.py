from bmc import bmc_app, db
from bmc.models import User, Practice

if (__name__ == '__main__'):
    bmc_app.run(debug=True)

@bmc_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Practice': Practice}
    