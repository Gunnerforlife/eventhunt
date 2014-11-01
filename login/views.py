from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
# Create your views here.

def login(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('login/home.html', context_instance=context)