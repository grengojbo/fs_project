# -*- mode: python; coding: utf-8; -*-

import logging
import os, os.path, sys

LOCAL_DEV = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEBUG_SQL = False # Show debug information about sql queries at the bottom of page
ORM_DEBUG = False

PROJECT_ROOT = DIRNAME = os.path.dirname(__file__)

#These are used when loading the test data
SITE_DOMAIN = "localhost"
SITE_NAME = "FreeSWITCH Admin Example (jbo)"

_parent = lambda x: os.path.normpath(os.path.join(x, '..'))
SATCHMO_DIRNAME = _parent(_parent(DIRNAME))
    
gettext_noop = lambda s:s

LANGUAGE_CODE = 'ru-ru'
LANGUAGES = (
   ('en', gettext_noop('English')),
   ('ru', gettext_noop('Russian')),
)


#DATABASE_ENGINE = 'mysql'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
# The following variables should be configured in your local_settings.py file
#DATABASE_NAME = 'freeswitch'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'freeswitch'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'YEhyt9FYs6KSBeq' # Not used with sqlite3.
#DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '3306'             # Set to empty string for default. Not used with sqlite3.
#DATABASE_OPTIONS = {
#    "init_command": "SET FOREIGN_KEY_CHECKS = 0",
#    "init_command": "SET storage_engine=INNODB",
#} 

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(DIRNAME, 'fs.db')

##### For Email ########
# If this isn't set in your settings file, you can set these here
#DEFAULT_FROM_EMAIL = ''
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True


#
START_PHONE_NUMBER = 2000000
START_ACCOUNTCODE = 2000
# default limit seconds
LIM_TIME=120


CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60*5
CACHE_PREFIX = "S"

# Admin Site Title
ADMIN_HEADLINE = 'FreeSWITCH Admin'
ADMIN_TITLE = 'FreeSWITCH Admin'
# Link to your Main Admin Site (no slashes at start and end)
ADMIN_URL = '/admin/'

#Configure logging
LOGFILE = "fsa.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

fileLog = logging.FileHandler(os.path.join(DIRNAME, LOGFILE), 'w')
fileLog.setLevel(logging.DEBUG)
# add the handler to the root logger
logging.getLogger('').addHandler(fileLog)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)
logging.info("FreeSWITCH Web Admin start")
