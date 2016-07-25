

import os

from flask import Flask, render_template, redirect, url_for

from stacks.corpus.models import Corpus, Export

from .forms import ExportForm


app = Flask(__name__)

# TODO: ENV-ify.
app.secret_key = 'dev'


@app.route('/export', methods=['GET', 'POST'])
def query():

    """
    Render the corpus query form.
    """

    form = ExportForm()

    if form.validate_on_submit():
        return redirect(url_for('download', uuid='123'))

    else:

        corpora = Corpus.query.all()

        return render_template('export/query.html',
            form=form,
            corpora=corpora,
        )


@app.route('/download/<uuid>')
def download(uuid):

    """
    Provide a download link.
    """

    return render_template('export/download.html')
