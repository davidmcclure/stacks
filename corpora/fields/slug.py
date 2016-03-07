

from django.db import models

from corpora.validators import validate_slug


class SlugField(models.CharField):


    validators = [validate_slug]
    unique = True
