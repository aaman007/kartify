from .base import *

# SECURITY WARNING: don't run with debug turned on in production.txt!
DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'kartify/static'
STATICFILES_DIRS = [
    'kartify/static_local'
]

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'kartify/media'
