

import rq_dashboard
import os

from flask import Flask


app = Flask(__name__)

app.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')
app.config.from_object(rq_dashboard.default_settings)
