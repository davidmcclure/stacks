

from voluptuous import Schema, Optional, Invalid


schema = Schema({

    'identifier': str,
    'title': str,
    'plain_text': str,

    Optional('author'): {
        Optional('name'): {
            Optional('full'): str,
            Optional('first'): str,
            Optional('last'): str,
        }
    },

    Optional('year'): int,

}, required=True)
