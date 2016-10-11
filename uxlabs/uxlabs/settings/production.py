from .base import *


DEBUG = False

ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INSTALLED_APPS += []
