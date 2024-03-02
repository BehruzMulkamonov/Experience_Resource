from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from adminstration.forms import LibraryCategoryForm, LibraryForm
from other_app.models import Library
from resources.models import PeriodFilter




class LibraryListView(ListView):
    model = Library
    template_name = 'other_app/library/list.html'
    context_object_name = 'libraries'


class LibraryCreateView(CreateView):
    model = Library
    form_class = LibraryForm
    template_name = 'other_app/library/create_update.html'
    success_url = reverse_lazy('library_list')


class LibraryUpdateView(UpdateView):
    model = Library
    form_class = LibraryForm
    template_name = 'other_app/library/create_update.html'
    success_url = reverse_lazy('library_list')




class LibraryDeleteView(DeleteView):
    model = Library
    template_name = 'other_app/library/delete.html'
    success_url = reverse_lazy('library_list')
    context_object_name ='library' # Ma'lumot o'chirilgandan keyin qaytish joyi

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))















