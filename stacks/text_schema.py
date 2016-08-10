

from voluptuous import Schema, Optional, Any


schema = Schema({

    'identifier': str,
    'title': str,
    'plain_text': str,

    'author': {
        'name': {
            'full': Any(str, None),
            'first': Any(str, None),
            'last': Any(str, None),
        }
    },

    'year': Any(int, None),

}, required=True)
