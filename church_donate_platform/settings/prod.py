# settings/prod.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or 'mssql' with pyodbc for Azure SQL
        'NAME': os.getenv('AZURE_DB_NAME'),
        'USER': os.getenv('AZURE_DB_USER'),
        'PASSWORD': os.getenv('AZURE_DB_PASSWORD'),
        'HOST': os.getenv('AZURE_DB_HOST'),
        'PORT': os.getenv('AZURE_DB_PORT', '1433'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'  # or your SMTP provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = 'yourchurch@example.com'
