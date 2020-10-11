from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from cats.models import Cat,Breed
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View

# Create your views here.

class CatList(LoginRequiredMixin,View):
    def get(self,request):
        cat=Cat.objects.all()
        breed=Breed.objects.all().count()
        context={'cat':cat, 'breed':breed}
        return render(request,"cats/cat_list.html",context)

class BreedList(LoginRequiredMixin,View):
    def get(self,request):
        breed=Breed.objects.all()
        context={'breed':breed}
        return render(request,"cats/breed_list.html",context)

class CatCreate(LoginRequiredMixin,CreateView):
    model=Cat
    fields="__all__"
    success_url=reverse_lazy("cats:all")

class CatUpdate(LoginRequiredMixin,UpdateView):
    model=Cat
    fields="__all__"
    success_url=reverse_lazy("cats:all")

class CatDelete(LoginRequiredMixin,DeleteView):
    model=Cat
    fields="__all__"
    success_url=reverse_lazy("cats:all")

class BreedCreate(LoginRequiredMixin,CreateView):
    model=Breed
    fields="__all__"
    success_url=reverse_lazy("cats:all")

class BreedUpdate(LoginRequiredMixin,UpdateView):
    model=Breed
    fields="__all__"
    success_url=reverse_lazy("cats:all")

class BreedDelete(LoginRequiredMixin,DeleteView):
    model=Breed
    fields="__all__"
    success_url=reverse_lazy("cats:all")