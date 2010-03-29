# -*- mode: python; coding: utf-8; -*-

import logging
import os, os.path

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = DIRNAME = os.path.dirname(__file__)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(DIRNAME, 'fs.db')

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)


MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# trick to get the two-levels up directory, which for the "large" project should be the satchmo dir
# for most "normal" projects, you should directly set the SATCHMO_DIRNAME, and skip the trick
_parent = lambda x: os.path.normpath(os.path.join(x, '..'))
SATCHMO_DIRNAME = _parent(_parent(DIRNAME))
    
# since we don't have any custom media for this project, lets just use Satchmo's
#MEDIA_ROOT = os.path.join(SATCHMO_DIRNAME, 'static/')

gettext_noop = lambda s:s

LANGUAGES = (
   ('ru', gettext_noop('Russian')),
   ('en', gettext_noop('English')),
)

# Only set these if Satchmo is part of another Django project
#These are used when loading the test data
#SITE_NAME = "large"
#MEDIA_ROOT = os.path.join(SATCHMO_DIRNAME, 'static/')
#DJANGO_PROJECT = 'large'
#DJANGO_SETTINGS_MODULE = 'large.settings'

# "large" doesn't have any custom templates, usually you'd have one here for your site.
TEMPLATE_DIRS = (
    os.path.join(DIRNAME, "templates"),
)


##### For Email ########
# If this isn't set in your settings file, you can set these here
DEFAULT_FROM_EMAIL = 'web@exempla.com'
EMAIL_HOST = 'localhost'
#EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True

REQUIRE_EMAIL_CONFIRMATION = False

# если используется Google Data APIs
#GOOGLE_MAPS_API_KEY = ''
DEFAULT_AVATAR = os.path.join(MEDIA_ROOT, 'avatars', 'generic.jpg')
DEFAULT_AVATAR_WIDTH = 96
AVATAR_WEBSEARCH = False
# Поиск аваторов
# AVATAR_WEBSEARCH = True
#

#These are used when loading the test data
#SITE_DOMAIN = "localhost"
#SITE_NAME = "Large Satchmo"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
#CACHE_BACKEND = "locmem:///"
#CACHE_TIMEOUT = 60*5
#CACHE_PREFIX = "S"

#ACCOUNT_ACTIVATION_DAYS = 7

START_ACCOUNTCODE = 2000
START_PHONE_NUMBER = 2000005
# default limit seconds
LIM_TIME=120
#Configure logging
LOGFILE = "fsadmin.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

fileLog = logging.FileHandler(os.path.join(DIRNAME, LOGFILE), 'w')
fileLog.setLevel(logging.DEBUG)
# add the handler to the root logger
logging.getLogger('').addHandler(fileLog)
##logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.info("FreeSWITCH Web Admin start")
