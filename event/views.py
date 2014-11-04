from django.shortcuts import render,render_to_response, RequestContext
from django.contrib.auth.models import User
from .models import Event
# Create your views here.

def add(request):
    return render_to_response('event/addevent.html', locals(),context_instance=RequestContext(request))

def added(request):
    event = Event()
    event.name = request.POST.get("name", "")
    event.description = request.POST.get("desc", "")
    print 'data'
    print event.name, event.description
    userId = request.session['userid']
    print userId
    event.user = User.objects.get(id=userId)
    print event.user
    print type(event)
    event.save()
    return render_to_response('login/home.html', locals(),context_instance=RequestContext(request))
