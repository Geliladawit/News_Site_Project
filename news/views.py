from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy 
from .models import News
class NewsListView(ListView):
    model = News
    template_name = 'news.html'
class NewsDetailView(DetailView): 
    model = News
    template_name = 'news_detail.html'
class NewsUpdateView(UpdateView): 
    model = News
    fields = ('title', 'body',)
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news')
class NewsDeleteView(DeleteView): 
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')
class NewsCreateView(CreateView):
    model = News
    template_name = 'news_new.html'
    fields = ('title', 'body', 'author',)
    success_url = reverse_lazy('news')
