from conf.common import *
from S3 import CallingFormat

DEBUG = False 
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

STATIC_URL = 'http://s3.amazonaws.com/droptype/'
MEDIA_URL = 'http://s3.amazonaws.com/droptype/'
THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'droptype'
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

