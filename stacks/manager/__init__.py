

import os

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def stacks():
    return render_template('query.html')
