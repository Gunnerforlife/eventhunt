import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from event.models import Event
from .models import Eve_Upvote
# Create your views here.

def eve_upvote(request):
    vars = {}
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        event = get_object_or_404(Event, name=slug)
        print user, slug, event

        try:
            user_old = Eve_Upvote.objects.get(event=event)
        except:
            user_old = None

        print user_old

        if user_old:
            try:
                existing_user = user_old.user.get(username=request.user.username)
            except:
                existing_user = None
            print existing_user
            if existing_user:
                user_old.user.remove(request.user)
                user_old.total_upvotes -= 1
                user_old.save()
            else:
                user_old.user.add(request.user)
                user_old.total_upvotes += 1
                user_old.save()
        else:
            print 'in else'
            user_new = Eve_Upvote.objects.create(event=event)
            print user_new
            user_new.user.add(request.user)
            user_new.total_upvotes += 1
            user_new.save()
    return HttpResponse(json.dumps(vars), content_type='application/javascript')
