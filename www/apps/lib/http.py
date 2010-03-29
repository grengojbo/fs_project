# -*- mode: python; coding: utf-8; -*-

from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from lib.helpers import reverse

def render_response(request, tmpl, output):
    return render_to_response(tmpl, output, context_instance=RequestContext(request))

class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` mimetype.
    """
    def __init__(self, data):
        super(JsonResponse, self).__init__(content=simplejson.dumps(data), mimetype='application/json')

class HttpResponseRedirectView(HttpResponseRedirect):
    """
    This response directs to a view by reversing the url
    e.g. return HttpResponseRedirectView('org.myself.views.myview') 
    or use the view object e.g.
    from org.myself.views import myview
    return HttpResponseRedirectView(myview)
    
    You can also pass the url arguments to the constructor e.g.
    return HttpResponseRedirectView('org.myself.views.myview', year=2008, colour='orange')
    """
    def __init__(self, view, *args, **kwargs):
        viewurl = reverse(view, args=args, kwargs=kwargs)
        HttpResponseRedirect.__init__(self, viewurl)

