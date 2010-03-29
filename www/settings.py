# -*- mode: python; coding: utf-8; -*-  
# Django settings for satchmo project.
# If you have an existing project, then ensure that you modify local_settings-customize.py
# and import it from your main settings file. (from local_settings import *)
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import os, sys

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))

DJANGO_PROJECT = 'fsa'
DJANGO_SETTINGS_MODULE = 'settings'

ADMINS = (
     ('', ''),
)

MANAGERS = ADMINS


# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'ru'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
I18N_URLS = False
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/static/')
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

SITE_ID = 1

#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static/')
#MEDIA_URL = '/static/'
MEDIA_URL = '/media/'
#STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/admin-media/'
ADMIN_MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/admin/') 
if not hasattr(globals(), 'SECRET_KEY'):
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    #"django.contrib.csrf.middleware.CsrfMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "djanjinja.middleware.RequestContextMiddleware",
    #'grappelli.middleware.JavaScript404Patch',
    #"django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.auth',
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "sugar.context_processors.admin_media_prefix",
    "sugar.context_processors.settings_vars",
    )

TEMPLATE_DIRS = (
    #os.path.realpath(os.path.join(PROJECT_PATH, '../contrib/grappelli/templates/')),
    os.path.join(PROJECT_ROOT, "templates"),
)

ROOT_URLCONF = 'urls'
#AUTH_PROFILE_MODULE = 'contact.contact'

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admindocs',
    #'django.contrib.comments',
    'django.contrib.sessions',
    #'django.contrib.sitemaps',
    'django_extensions',
    #'django.contrib.flatpages',
    'signals_ahoy',
    'djanjinja',
    'sugar',
    'keyedcache',
    'livesettings',
    'l10n',
    'south',
    'shoes',
    'app_plugins',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
DJANJINJA_BUNDLES = (
    'djanjinja.cache',
    'djanjinja.humanize',
    'djanjinja.site',
)
# JINJA_EXTENSIONS = (
#     'jinja2.ext.i18n', # i18n Extension
# )
from django.conf.urls.defaults import patterns, include
# Load the local settings
try:
    from settings_local import *
except ImportError:
    import sys
    sys.stderr.write('Unable to read settings_local.py\n')
    sys.exit(1)
try:
    from fsa.fsa_settings import *
except ImportError:
    sys.stderr.write('Unable to read fsa_settings.py\n')
try:
    from fsb.fsb_settings import *
except ImportError:
    sys.stderr.write('Unable to read fsb_settings.py\n')
try:
    from debug_settings import *
except ImportError:
    sys.stderr.write('Unable to read debug_settings.py\n')