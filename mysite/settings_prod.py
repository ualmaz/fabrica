from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'customers',
        'USER': 'ualmaz',
        'PASSWORD': '197791515Almaz',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}