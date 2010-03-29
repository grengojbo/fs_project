# -*- mode: python; coding: utf-8; -*-

from time import localtime, strftime
from os.path import join, exists, isdir, getmtime
from django.utils._os import safe_join
from django import template
from django.conf import settings

def gettime(filename):
    time = localtime(getmtime(filename))
    return strftime('%Y%m%d%H%M', time)

def _static(static_url, static_root, path):
    fullpath = safe_join(static_root, path)
    if exists(fullpath) and not isdir(fullpath):
        url = '%s%s' % (static_url, path)
        if settings.APPEND_MTIME_TO_STATIC:
            url = '%s?%s' % (url, gettime(fullpath))
        return {'include': True, 'url': url}
    return {'include': False}

def global_static(path):
    return _static(
        settings.STATIC_URL,
        settings.STATIC_ROOT,
        path)

def theme_static(path):
    return _static(
        settings.THEME_STATIC_URL,
        settings.THEME_STATIC_ROOT,
        path)

register = template.Library()

class StaticCssNode(template.Node):
    def __init__(self, filename, media=None,
                 use_global_static=False):
        self.filename = template.Variable(filename)
        self.use_global_static = use_global_static
        if media:
            self.media = template.Variable(media)
        else:
            self.media = None
    
    def render(self, context):
        try:
            filename = self.filename.resolve(context)
            if self.media:
                media = self.media.resolve(context)
            else:
                media = None
        except template.VariableDoesNotExist:
            return ''
        if not filename.endswith('.css'):
            filename = 'css/%s.css' % filename
        if self.use_global_static:
            data = global_static(filename)
            place = 'global static'
        else:
            data = theme_static(filename)
            place = 'theme static'
        if data['include']:
            if media:
                return '<link rel="stylesheet" type="text/css" href="%s" media="%s">' % \
                        (data['url'], media)
            else:
                return '<link rel="stylesheet" type="text/css" href="%s">' % data['url']
        else:
            return '<!-- missing css %s in %s -->' % (filename, place)

def _do_static_css(parser, token):
    parsed_tag = token.split_contents()
    if len(parsed_tag) < 2 or len(parsed_tag) > 3:
        raise template.TemplateSyntaxError, "%r tag requires 2 or 3 arguments"
    tag_name, css_filename, css_media = parsed_tag[0], parsed_tag[1], None
    if len(parsed_tag) == 3:
        css_media = parsed_tag[2]
    return tag_name, css_filename, css_media

@register.tag(name='global_css')
def do_global_css(parser, token):
    tag_name, css_filename, css_media = _do_static_css(parser, token)
    return StaticCssNode(css_filename, css_media, use_global_static=True)

@register.simple_tag
def global_js(filename):
    if not filename.endswith('.js'):
        filename = 'js/%s.js' % filename
    global_data = global_static(filename)
    if global_data['include']:
        return '<script type="text/javascript" src="%s"></script>' % global_data['url']
    else:
        return '<!-- missing js %s in global static -->' % filename

@register.simple_tag
def global_staticfile(filename):
    global_data = global_static(filename)
    if global_data['include']:
        return global_data['url']
    else:
        return ''

@register.tag(name='theme_css')
def do_theme_css(parser, token):
    tag_name, css_filename, css_media = _do_static_css(parser, token)
    node =  StaticCssNode(css_filename, css_media, use_global_static=False)
    return node

@register.simple_tag
def theme_js(filename):
    if not filename.endswith('.js'):
        filename = 'js/%s.js' % filename
    theme_data = theme_static(filename)
    if theme_data['include']:
        return '<script type="text/javascript" src="%s"></script>' % theme_data['url']
    else:
        return '<!-- missing js %s in theme static -->' % filename

@register.simple_tag
def theme_staticfile(filename):
    theme_data = theme_static(filename)
    if theme_data['include']:
        return theme_data['url']
    else:
        return ''

