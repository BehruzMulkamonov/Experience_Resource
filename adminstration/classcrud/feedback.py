from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from adminstration.forms import FeedbacksForm
from other_app.models import Feedbacks


class FeedbacksCreateView(CreateView):
    model = Feedbacks
    form_class = FeedbacksForm
    template_name = 'other_app/feedback/create_update.html'
    success_url = reverse_lazy('feedback_list')

class FeedbacksUpdateView(UpdateView):
    model = Feedbacks
    form_class = FeedbacksForm
    template_name = 'other_app/feedback/create_update.html'
    success_url = reverse_lazy('feedback_list')

class FeedbacksDeleteView(DeleteView):
    model = Feedbacks
    template_name = 'other_app/feedback/delete.html'
    success_url = reverse_lazy('feedback_list')
    context_object_name = 'feedback'


class FeedbacksListView(ListView):
    model = Feedbacks
    template_name = 'other_app/feedback/list.html'
    context_object_name = 'feedbacks'

