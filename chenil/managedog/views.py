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
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = DogModelForm()
            context = {"form": form}
            template = loader.get_template('managedog/form.html')
            return HttpResponse(template.render(context,request))
        else:
            form = DogModelForm(request.POST)
            if form.is_valid():
                form.save()
            # reset la page
            return redirect('/')
    else:
        return HttpResponse('<h1>Vous devez être connecté pour créer un chien</h1>')


def delete(request, dog_pk):
    if request.user.is_authenticated:
        Dog.objects.get(id=dog_pk).delete()
        return redirect('/')
    else:
        return HttpResponse('<h1>Vous devez être connecté pour supprimer un chien</h1>')
        

def details(request, dog_pk):
    template = loader.get_template('managedog/details.html')
    dog = Dog.objects.get(id=dog_pk)
    form = DogModelForm(instance=dog)
    context = {"form": form,"dog": dog}

    return HttpResponse(template.render(context,request))


def edit(request,dog_pk):
    if request.user.is_authenticated:
        if request.method == "GET":
            template = loader.get_template('managedog/edit.html')
            dog = Dog.objects.get(id=dog_pk)
            form = DogModelForm(instance=dog)
            context = {"form": form,"dog": dog}

            return HttpResponse(template.render(context,request))
        else:
            instance = get_object_or_404(Dog, id=dog_pk)
            form = DogModelForm(request.POST,instance=instance)
            if form.is_valid():
                form.save()

            return redirect('/')
    else:
        return HttpResponse('<h1>Vous devez être connecté pour éditer un chien</h1>')
