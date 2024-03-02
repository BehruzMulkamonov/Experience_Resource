from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from adminstration.forms import CommentsForm
from other_app.models import Comments


class CommentsCreateView(CreateView):
    model = Comments
    form_class = CommentsForm
    template_name = 'other_app/comment/create_update.html'
    success_url = reverse_lazy('comment_list')

class CommentsUpdateView(UpdateView):
    model = Comments
    form_class = CommentsForm
    template_name = 'other_app/comment/create_update.html'
    success_url = reverse_lazy('comment_list')

class CommentsDeleteView(DeleteView):
    model = Comments
    template_name = 'other_app/comment/delete.html'
    success_url = reverse_lazy('comment_list')
    context_object_name = 'comment'


class CommentsListView(ListView):
    model = Comments
    template_name = 'other_app/comment/list.html'
    context_object_name = 'comments'

