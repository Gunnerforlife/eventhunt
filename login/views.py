from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.template import loader
from event.models import Event
from django.template.context import RequestContext
# Create your views here.

def login(request):
    request.session['userid'] = request.user.id
    template = loader.get_template('login/home.html')
    print request.user.id
    events_list = Event.objects.all()
    print events_list
    context = RequestContext(request, {'request': request, 'user': request.user, 'events_list': events_list})
    #return render_to_response('login/home.html', context_instance=context)
    return HttpResponse(template.render(context))