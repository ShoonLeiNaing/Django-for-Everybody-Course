from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from autos.models import Make,Auto
from autos.forms import MakeForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class MainView(LoginRequiredMixin, View):
    def get(self,request):
        mc=Make.objects.all().count()
        al=Auto.objects.all()
        context={"make_count":mc ,"auto_list":al}
        return render(request,"autos/auto_list.html",context)



class MakeView(LoginRequiredMixin, View):
    def get(self,request):
        mc=Make.objects.all()
        context={"make_list":mc}
        return render(request,"autos/make_list.html",context)



class MakeCreate(LoginRequiredMixin, View):
    template="autos/make_form.html"
    success_url=reverse_lazy('autos:all')
    def get(self,request):
        form=MakeForm()
        context={'form':form}
        return render(request,self.template,context)

    def post(self,request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            context={'form':form}
            return render(request,self.template,context)

        make=form.save()
        return redirect(self.success_url)



class MakeUpdate(LoginRequiredMixin,View):
    model=Make
    template="autos/make_form.html"
    success_url=reverse_lazy('autos:all')
    def get(self,request,pk):
        make=get_object_or_404(self.model, pk=pk)
        form=MakeForm(instance=make)
        context={'form':form}
        return render(request,self.template,context)

    def post(self,request,pk):
        make=get_object_or_404(self.model, pk=pk)
        form=MakeForm(request.POST, instance=make)
        if not form.is_valid():
            context={'form':form}
            return render(request,self.template,context)

        form.save()
        return redirect(self.success_url)


class MakeDelete(LoginRequiredMixin,View):
    model=Make
    template="autos/make_confirm_delete.html"
    success_url=reverse_lazy('autos:all')
    def get(self,request,pk):
        make=get_object_or_404(self.model, pk=pk)
        form=MakeForm(instance=make)
        context={'make':make}
        return render(request,self.template,context)

    def post(self,request,pk):
        make=get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)



class AutoCreate(LoginRequiredMixin, CreateView):
    model=Auto
    fields="__all__"
    success_url=reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model=Auto
    fields="__all__"
    success_url=reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model=Auto
    fields="__all__"
    success_url=reverse_lazy('autos:all')






