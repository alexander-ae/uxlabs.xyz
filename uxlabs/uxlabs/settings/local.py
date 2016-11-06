from .base import *


ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS')

STATIC_URL = ENV.get('STATIC_URL')
STATIC_ROOT = ''

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = ENV.get('MEDIA_URL')

INSTALLED_APPS += []
