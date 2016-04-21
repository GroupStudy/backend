from django.http import HttpResponse

from django.template import RequestContext, loader

from . import models



def index(request):
    template = loader.get_template('study/test.html')

    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

