from django.shortcuts import render,render_to_response

# Create your views here.

def add(request):
    return render_to_response('event/addevent.html')