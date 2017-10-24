"""
Django settings for cadetapp project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h&1ro2g+^oq=e57iv&^^d#*k80&5zw07%h9ng1p_)%jy6jx(5s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'cadetsandbox.pythonanywhere.com']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'pipeline',   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cadetapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dashboard/templates/dashboard')],
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

WSGI_APPLICATION = 'cadetapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/public/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_final')
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# STATIC_ROOT = '/Users/akh/WWW/CADET_Sandbox/cadetapp/assets'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "public"),
)

## Add storage for pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage' 

# Add PipelineFinder 
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',

)

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

# Config on assets for pipeline

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'maincss': {
            'source_filenames': (
                'css/sb-admin.css',
            ),
            'output_filename': 'css/main-compiled.css',
            'variant': 'datauri',
        },
        'vendorcss': {
            'source_filenames': (
                'css/bootstrap/css/bootstrap.css',
                'css/bootstrap/css/bootstrap-grid.css',
                'css/bootstrap/css/bootstrap-reboot.css.css',
            ),
            'output_filename': 'css/vendors-compiled.css',
        }
    },
    'JAVASCRIPT': {
        'mainjs': {
            'source_filenames': (
                'js/jquery/jquery.js',
                'js/bootstrap.js',
                'js/jquery.easing.js',
                'js/jquery.easing.compatibility.js',
                'js/popper.min.js',
                'js/sb-admin-databases.js',
                'js/sb-admin.js',
            ),
            'output_filename': 'js/main-compiled.js',
        }
    }
}

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
