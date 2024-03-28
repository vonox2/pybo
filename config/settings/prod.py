from .base import *

ALLOWED_HOSTS = ['52.79.104.162']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'otu4^Ceao]$WjT;hLUac$KMcughaK#:,',
        'HOST': 'ls-d752fd884373e707741c861a374706734b11a371.cr0koe0mqklv.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}