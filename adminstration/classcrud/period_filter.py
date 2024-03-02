# from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminstration.forms import PeriodFilterForm
# from django.urls import reverse_lazy
#
# from adminstration.forms import PeriodFilterForm
from resources.models import PeriodFilter


#

class PeriodFilterCreateView(CreateView):
    model = PeriodFilter
    form_class = PeriodFilterForm
    print(PeriodFilterForm())
    template_name = 'resources/period_filters/create_update.html'
    success_url = reverse_lazy('period-filter-list')


#
class PeriodFilterUpdateView(UpdateView):
    model = PeriodFilter
    form_class = PeriodFilterForm
    template_name = 'resources/period_filters/create_update.html'
    success_url = reverse_lazy('period-filter-list')


class PeriodFilterDeleteView(DeleteView):
    model = PeriodFilter
    template_name = 'resources/period_filters/delete.html'
    success_url = reverse_lazy('period-filter-list')
    context_object_name = 'period_filter'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))


class PeriodFilterListView(ListView):
    model = PeriodFilter
    template_name = 'resources/period_filters/period_filters_list.html'
    context_object_name = 'period_filters'
