from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def login(request):
    template = loader.get_template('login/home.html')
    context = locals()
    return render_to_response('login/home.html',locals(),context_instance = RequestContext(request))