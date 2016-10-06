from django.http import HttpResponse
from django.template import loader
from django.template import Template
from django.shortcuts import render
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context, request))