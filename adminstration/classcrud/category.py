from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from adminstration.forms import CategoryForm
from resources.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'resources/category/list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'resources/category/create_update.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'resources/category/create_update.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'resources/category/delete.html'  # O'chirishni tasdiqlash sahifasi
    success_url = reverse_lazy('category-list')
    context_object_name = 'category'  # Ma'lumot o'chirilgandan keyin qaytish joyi

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))
