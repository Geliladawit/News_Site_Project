from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Sport
class SportListView(ListView):
    model = Sport
    template_name = 'sport.html'
class SportDetailView(DetailView): 
    model = Sport
    template_name = 'sport_detail.html'
class SportUpdateView(UpdateView): 
    model = Sport
    fields = ('title', 'body',)
    template_name = 'sport_edit.html'
    success_url = reverse_lazy('sport')
class SportDeleteView(DeleteView):
    model = Sport
    template_name = 'sport_delete.html'
    success_url = reverse_lazy('sport')
class SportCreateView(CreateView):
    model = Sport
    template_name = 'sport_new.html'
    fields = ('title', 'body', 'author',)
    success_url = reverse_lazy('sport')

