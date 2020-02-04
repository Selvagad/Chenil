from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import requests

from .models import Dog
from .forms import DogModelForm

# Create your views here.
def index(request):
    template = loader.get_template('managedog/index.html')
    dog_list = list(Dog.objects.all())
    context = {"dogs":dog_list}
    return HttpResponse(template.render(context,request))

def create(request):
    if request.method == 'GET':
        form = DogModelForm()
        context = {"form": form}
        template = loader.get_template('managedog/form.html')
        return HttpResponse(template.render(context,request))
    else:
        form = DogModelForm(request.POST)
        if form.is_valid():
            form.save()
        # else:
            # TODO gerer le rendu des erreurs
        # reset la page
        return redirect('/managedog')