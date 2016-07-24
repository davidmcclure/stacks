

import os

from flask import Flask, render_template

from stacks.corpus.models import Corpus


app = Flask(__name__)


@app.route('/export')
def query():

    """
    Render the corpus query form.
    """

    corpora = Corpus.query.all()

    return render_template('export/query.html', corpora=corpora)
