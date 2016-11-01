from .base import *

if os.getenv('TRAVIS_BUILD', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travis_ci_test',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
        }
    }
else:
    DATABASES['default'] = dj_database_url.config()