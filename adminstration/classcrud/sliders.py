from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from adminstration.forms import SlidersForm
from other_app.models import Sliders


class SliderCreateView(CreateView):
    model = Sliders
    form_class = SlidersForm
    template_name = 'other_app/slider/create_update.html'
    success_url = reverse_lazy('slider_list')

class SliderUpdateView(UpdateView):
    model = Sliders
    form_class = SlidersForm
    template_name = 'other_app/slider/create_update.html'
    success_url = reverse_lazy('slider_list')

class SliderDeleteView(DeleteView):
    model = Sliders
    template_name = 'other_app/slider/delete.html'
    success_url = reverse_lazy('slider_list')
    context_object_name = 'slider'


class SliderListView(ListView):
    model = Sliders
    template_name = 'other_app/slider/list.html'
    context_object_name = 'sliders'

