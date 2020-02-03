from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import requests

from .models import Dog

# Create your views here.
def index(request):
    template = loader.get_template('managedog/index.html')
    context = {"name":'toto'}
    return HttpResponse(template.render(context,request))