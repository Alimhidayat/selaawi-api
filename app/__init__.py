from flask import Flask, copy_current_request_context, current_app
from threading import Thread, current_thread
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.extensions import db
import time
import random

from app.blueprints.dashboard.models.Dashboard import Dashboard
from app.blueprints.real_time.models.RealTime import RealTime
# from flask_migrate import Migrate

# registering blueprints
from app.blueprints.real_time.real_time import realTime, addDataRealTime
from app.blueprints.dashboard.bp_dashboard import dashboard, addDataDashboard




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///selaawi.db'

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(realTime)
app.register_blueprint(dashboard)


with app.app_context():
    Thread(target=addDataDashboard).start()
    Thread(target=addDataRealTime).start()
    


if __name__ == '__main__':
    app.run(debug=True)