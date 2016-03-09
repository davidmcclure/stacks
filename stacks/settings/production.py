

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stacks',
        'USER': 'stacks',
        'PASSWORD': '4wGnfZt4ZLaYa%z2',
    }
}


RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
}


STATIC_ROOT = '/opt/stacks/static'
