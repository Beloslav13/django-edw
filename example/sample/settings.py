# Django settings for sample project.
from __future__ import unicode_literals
import os
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured

EDW_APP_LABEL = 'sample'

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.path.split(PROJECT_DIR)[1]

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'edw_sample_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'ker7HgeejUE31TY',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
            ]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, r'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = r'/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('bower_components', os.path.join(PROJECT_PATH, 'bower_components')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)


ADMIN_MEDIA_PREFIX = '/static/admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'r=wi%2(qg34n&9hp1vub*vgsz0je2+5lu(!1zect6%qti=qegz'

# replace django.contrib.auth.models.User by implementation
# allowing to login via email address
AUTH_USER_MODEL = 'email_auth.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
        
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djng.middleware.AngularUrlMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'edw.middleware.CustomerMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'sample.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sample.wsgi.application'



TEMPLATES = [	{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': False,
    'DIRS': [],
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
    	    'django.template.context_processors.csrf',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'edw.context_processors.customer',
            'edw.context_processors.version',
        ),
        'loaders': [
	    'django.template.loaders.filesystem.Loader',
	    'django.template.loaders.app_directories.Loader',
        ]
    }
}]

INSTALLED_APPS = (
    'django.contrib.auth',
    'email_auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_select2',
    'adminsortable2',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_fsm',
    'fsm_admin',
    'djng',
    'compressor',
    'sekizai',
    'post_office',
    'filer',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'parler',
    'haystack',
    'edw.apps.EdwConfig',
    'sample.apps.SampleConfig',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

USE_X_FORWARDED_HOST = True

############################################
# settings for sending mail
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@example.com'
EMAIL_HOST_PASSWORD = 'smtp-secret-password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'My Shop <no-reply@example.com>'
EMAIL_REPLY_TO = 'info@example.com'
EMAIL_BACKEND = 'post_office.EmailBackend'

############################################
# settings for third party Django apps
COERCE_DECIMAL_TO_STRING = True

FSM_ADMIN_FORCE_PERMIT = True

ROBOTS_META_TAGS = ('noindex', 'nofollow')

############################################
# settings for django-restframework and plugins

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
	    'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # can be disabled for production environments
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
}
        
SERIALIZATION_MODULES = {}

############################################
# settings for storing session data

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_SAVE_EVERY_REQUEST = True

############################################
# settings for storing files and images

FILER_ADMIN_ICON_SIZES = ('16', '32', '48', '80', '128')

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = False

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_OPTIMIZE_COMMAND = {
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}',
    'png': '/usr/bin/optipng {filename}'
}
            
THUMBNAIL_PRESERVE_EXTENSIONS = True
            
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

SELECT2_CSS = 'bower_components/select2/dist/css/select2.min.css'
SELECT2_JS = 'bower_components/select2/dist/js/select2.min.js'

#############################################
# settings for full index text search (Haystack)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
	'INDEX_NAME': 'edw_sample',
    }
}

HAYSTACK_ROUTERS = ('edw.search.routers.LanguageRouter',)

SILENCED_SYSTEM_CHECKS = ('auth.W004')