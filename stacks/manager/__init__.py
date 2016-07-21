

import os

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/export')
def stacks():
    return render_template('export/query.html')
