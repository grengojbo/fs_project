# -*- mode: python; coding: utf-8; -*-

from settings import *

LOCAL_DEV = True
TOOLBAR_DEV = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_SQL = False # Show debug information about sql queries at the bottom of page
ORM_DEBUG = False
#sorl-thumbnail
THUMBNAIL_DEBUG = True

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)
if TOOLBAR_DEV:
    MIDDLEWARE_CLASSES += (
        'sugar.middleware.debugging.UserBasedExceptionMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += ('debug_toolbar', )
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)
    DEBUG_TOOLBAR_CONFIG = {
       'INTERCEPT_REDIRECTS' : False,
    }
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

