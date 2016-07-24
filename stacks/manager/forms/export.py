

from flask_wtf import Form
from wtforms import SelectMultipleField, IntegerField
from wtforms.validators import DataRequired

from stacks.corpus.models import Corpus


class ExportForm(Form):

    corpora = SelectMultipleField(

        label='Corpora',

        choices=[
            (c.id, c.name)
            for c in Corpus.query.all()
        ],

        validators=[DataRequired()],

        coerce=int,

    )

    min_year = IntegerField(
        label='Start Year',
    )

    max_year = IntegerField(
        label='End Year',
    )

    sample_size = IntegerField(
        label='Sample Size',
    )
