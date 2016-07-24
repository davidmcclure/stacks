

from flask_wtf import Form
from wtforms import SelectMultipleField, IntegerField
from wtforms.validators import DataRequired


class ExportForm(Form):

    corpora = SelectMultipleField(
        validators=[DataRequired()],
    )

    min_year = IntegerField()

    max_year = IntegerField()

    sample_size = IntegerField()
