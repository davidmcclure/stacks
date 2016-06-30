

import rq_dashboard
import os

from flask import Flask


app = Flask(__name__)

# RQ dashboard
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')

# TODO: UI


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))
