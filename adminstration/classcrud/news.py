from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from adminstration.forms import NewsForm
from other_app.models import News


class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'other_app/news/create_update.html'
    success_url = reverse_lazy('news_list')

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'other_app/news/create_update.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'other_app/news/delete.html'
    success_url = reverse_lazy('news_list')
    context_object_name = 'new'


class NewsListView(ListView):
    model = News
    template_name = 'other_app/news/list.html'
    context_object_name = 'news'

