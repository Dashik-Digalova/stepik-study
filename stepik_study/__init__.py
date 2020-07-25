from flask import Flask

from stepik_study.config import Config
from stepik_study.models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from stepik_study.views import *

if __name__ == "__main__":
    app.run()

