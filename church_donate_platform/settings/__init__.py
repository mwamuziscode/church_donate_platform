# settings/base.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-dev-secret-key")

INSTALLED_APPS = [
    ...
]

MIDDLEWARE = [
    ...
]

ROOT_URLCONF = 'church_donation.urls'

TEMPLATES = [
    ...
]

WSGI_APPLICATION = 'church_donation.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
