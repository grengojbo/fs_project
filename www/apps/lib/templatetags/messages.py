# -*- mode: python; coding: utf-8; -*-

from django.template import Library
from django.contrib.auth.models import User

register = Library()

@register.inclusion_tag('lib/messages.html',takes_context=True)
def site_messages(context):
    sess = getattr(context['request'], 'session', {})
    return {
            'errors': sess.get('site_messages',{}).get('errors'),
            'notices': sess.get('site_messages', {}).get('notices')}
