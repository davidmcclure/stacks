

import os

from flask import Flask, render_template

from stacks.corpus.models import Corpus

from .forms import ExportForm


app = Flask(__name__)

# TODO: ENV-ify.
app.secret_key = 'dev'


@app.route('/export')
def query():

    """
    Render the corpus query form.
    """

    form = ExportForm()

    if form.validate_on_submit():
        pass

    else:

        corpora = Corpus.query.all()

        return render_template(
            'export/query.html',
            form=form,
            corpora=corpora,
        )
