# -*- coding: utf-8 -*-

from os.path import abspath, dirname
from optparse import make_option
from django.core.management.base import BaseCommand, NoArgsCommand
from django.conf import settings
from django.utils._os import safe_join
from django.contrib import admin
import os
import shutil

class Command(NoArgsCommand):
    help = "Copy the Admin Media directory and files to the local project."

    def handle_noargs(self, **options):
        #import satchmo_store
        admin_media_src = abspath(safe_join(dirname(abspath(admin.__file__)), 'media'))
        admin_media_desc = abspath(os.path.join(settings.PROJECT_ROOT, 'admin-media'))
        #static_src = os.path.join(satchmo_store.__path__[0],'../../static')
        #static_dest = os.path.join(os.getcwd(), 'static')
        #if os.path.exists(admin_media_src):
        #    print "Admin Media directory exists. You must manually copy the files you need."
        #else:

        shutil.copytree(admin_media_src,admin_media_desc)
        for root, dirs, files in os.walk(admin_media_desc):
            if '.svn' in dirs:
                shutil.rmtree(os.path.join(root,'.svn'), True)
            print "Copied %s to %s" % (admin_media_src, admin_media_desc)
