

from flask_wtf import Form
from wtforms import SelectMultipleField, IntegerField
from wtforms.validators import DataRequired, Optional

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
        description='Exclude texts published before this year.',
        validators=[Optional()],
    )

    max_year = IntegerField(
        label='End Year',
        description='Exclude texts published after this year.',
        validators=[Optional()],
    )

    sample_size = IntegerField(

        label='Sample Size',

        description='''Randomly sample N texts. If left blank, all texts that
        match the filters will be included.''',

        validators=[Optional()],

    )
