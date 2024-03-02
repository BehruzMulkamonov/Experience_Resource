from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from adminstration.forms import AboutForm
from other_app.models import About


class AboutCreateView(CreateView):
    model = About
    form_class = AboutForm
    template_name = 'other_app/about/create_update.html'
    success_url = reverse_lazy('about_list')

class AboutUpdateView(UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'other_app/about/create_update.html'
    success_url = reverse_lazy('about_list')

class AboutDeleteView(DeleteView):
    model = About
    template_name = 'other_app/about/delete.html'
    success_url = reverse_lazy('about_list')
    context_object_name = 'about'


class AboutListView(ListView):
    model = About
    template_name = 'other_app/about/list.html'
    context_object_name = 'abouts'

