# from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminstration.forms import FiltersForm
# from django.urls import reverse_lazy
#
# from adminstration.forms import FiltersForm
from resources.models import Filters


class FiltersListView(ListView):
    model = Filters
    template_name = 'resources/filters/list.html'
    context_object_name = 'filters'

class FiltersCreateView(CreateView):
    model = Filters
    form_class = FiltersForm
    template_name = 'resources/filters/create_update.html'
    success_url = reverse_lazy('filters-list')


class FiltersUpdateView(UpdateView):
    model = Filters
    form_class = FiltersForm
    template_name = 'resources/filters/create_update.html'
    success_url = reverse_lazy('filters-list')




class FilterDeleteView(DeleteView):
    model = Filters
    template_name = 'resources/filters/delete.html'
    success_url = reverse_lazy('filters-list')
    context_object_name ='filters' # Ma'lumot o'chirilgandan keyin qaytish joyi

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))



