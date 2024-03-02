from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from adminstration.forms import ConnectionForm
from other_app.models import Connection


class ConnectionCreateView(CreateView):
    model = Connection
    form_class = ConnectionForm
    template_name = 'other_app/connection/create_update.html'
    success_url = reverse_lazy('connection_list')

class ConnectionUpdateView(UpdateView):
    model = Connection
    form_class = ConnectionForm
    template_name = 'other_app/connection/create_update.html'
    success_url = reverse_lazy('connection_list')

class ConnectionDeleteView(DeleteView):
    model = Connection
    template_name = 'other_app/connection/delete.html'
    success_url = reverse_lazy('connection_list')
    context_object_name = 'connection'


class ConnectionListView(ListView):
    model = Connection
    template_name = 'other_app/connection/list.html'
    context_object_name = 'connections'

