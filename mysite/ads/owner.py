from django.views.generic import CreateView, UpdateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """

class OwnerListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerCreateView(LoginRequiredMixin,CreateView):

    def form_valid(self,form):
        object=form.save(commit=False)
        object.owner=self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin,UpdateView):

    def get_queryset(self):
        qs=super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerDeleteView(LoginRequiredMixin,DeleteView):

    def get_queryset(self):
        qs=super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)