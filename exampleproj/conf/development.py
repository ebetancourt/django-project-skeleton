from conf.common import *

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'exampleproj',
        'USER': 'exampleproj',
        'PASSWORD': 'exampleproj',
        'HOST': '',
        'PORT': '',
    }
}

INTERNAL_IPS = ('127.0.0.1', 'active.lo',)
