"""
Django settings for TurismoProject project.

Generated by 'django-admin startproject' using Django 2.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p9=3jt6h@tw#7)bmf0!7-5ca#4cc@s(gcuvb^a(ws@smbunj%_'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getcwd() == '/var/www/html/turismoservice':
    DEBUG = False
    ALLOWED_HOSTS = ['turismoapp.creatu.co']
else:
    DEBUG = True
    ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TurismoApp.apps.TurismoappConfig',
    'TurismoPlace.apps.TurismoplaceConfig',
    'TurismoRestApi.apps.TurismorestapiConfig',
    'TurismoHotel.apps.TurismohotelConfig',
    'TurismoTour.apps.TurismotourConfig',
    'geoposition',
    'rest_framework',
    'sequences.apps.SequencesConfig',
]

GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyD7xt9P8jVg7JrzhPBIdrHHRThGcsvMoCY'

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 4,
    'maxZoom': 15,
    'parentSelector': 'li.changeform-tabs-item',
    'isDjangoAdmin': True,
    'center': {'lat': -25.244695951306028, 'lng': -57.48046875}
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move',
    'position': {'lat': -25.244695951306028, 'lng': -57.48046875}
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TurismoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TurismoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
MEDIA_URL = '/media/'