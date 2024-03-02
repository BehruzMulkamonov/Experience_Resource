from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from adminstration.forms import EventForm
from other_app.models import Event


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'other_app/event/create_update.html'
    success_url = reverse_lazy('events_list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'other_app/event/create_update.html'
    success_url = reverse_lazy('events_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'other_app/event/delete.html'
    success_url = reverse_lazy('events_list')
    context_object_name = 'event'


class EventListView(ListView):
    model = Event
    template_name = 'other_app/event/list.html'
    context_object_name = 'events'

