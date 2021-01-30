from saipa.settings.base import *


SECRET_KEY = os.environ.get('SECRET_KEY', None)

if not SECRET_KEY:
    raise Exception('Add SECRET_KEY env variable, example: export SECRET_KEY=123456')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['saipa.ir']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True
