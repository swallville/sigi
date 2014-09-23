"""
Django settings for sigi project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname

import django.conf.global_settings as DEFAULT_SETTINGS


BASE_DIR = dirname(dirname(dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

ALLOWED_HOSTS = []

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'sigi.context_processors.charts_data',
)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    )

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'sigi.apps.contatos',
    'sigi.apps.servidores',
    'sigi.apps.parlamentares',
    'sigi.apps.mesas',
    'sigi.apps.casas',
    'sigi.apps.convenios',
    'sigi.apps.inventario',
    'sigi.apps.servicos',
    'sigi.apps.metas',
    'sigi.apps.ocorrencias',
    'sigi.apps.financeiro',
    'sigi.apps.diagnosticos',

    # Third-party apps
    'localflavor',
    'reporting',
    'django_extensions',
    'googlecharts',
    'treemenus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sigi.urls'
WSGI_APPLICATION = 'sigi.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'pt-br'
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'sigiStatic'),
)

SERVER_EMAIL = 'sigi@interlegis.leg.br'
DEFAULT_FROM_EMAIL = 'spdt@interlegis.leg.br'
EMAIL_SUBJECT_PREFIX = u'[SIGI]'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True