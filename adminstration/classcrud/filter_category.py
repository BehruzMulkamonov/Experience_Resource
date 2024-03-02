# from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminstration.forms import FilterCategoryForm
# from django.urls import reverse_lazy
#
# from adminstration.forms import FilterCategoryForm
from resources.models import FilterCategories


class FilterCategoryListView(ListView):
    model = FilterCategories
    template_name = 'resources/filter_categories/list.html'
    context_object_name = 'filter_categories'


class FilterCategoryCreateView(CreateView):
    model = FilterCategories
    form_class = FilterCategoryForm
    template_name = 'resources/filter_categories/create_update.html'
    success_url = reverse_lazy('filter-category-list')


class FilterCategoryUpdateView(UpdateView):
    model = FilterCategories
    form_class = FilterCategoryForm
    template_name = 'resources/filter_categories/create_update.html'
    success_url = reverse_lazy('filter-category-list')


class FilterCategoryDeleteView(DeleteView):
    model = FilterCategories
    template_name = 'resources/filter_categories/delete.html'
    success_url = reverse_lazy('filter-category-list')
    context_object_name = 'filter_category'


    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))