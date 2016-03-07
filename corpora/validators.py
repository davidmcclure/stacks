

from django.core.validators import RegexValidator


validate_slug = RegexValidator(
    regex='^[a-z0-9-]+$',
    message='Lowercase letters and dashes.',
    code='invalid_slug',
)
