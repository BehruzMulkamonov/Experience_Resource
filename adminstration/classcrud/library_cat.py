# from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminstration.forms import LibraryCategoryForm
from other_app.models import Library_Category


# from django.urls import reverse_lazy
#
# from adminstration.forms import Library_CategoryForm


class Library_CategoryListView(ListView):
    model = Library_Category
    template_name = 'other_app/library_cat/list.html'
    context_object_name = 'library_cats'


class Library_CategoryCreateView(CreateView):
    model = Library_Category
    form_class = LibraryCategoryForm
    template_name = 'other_app/library_cat/create_update.html'
    success_url = reverse_lazy('library_cat_list')


class Library_CategoryUpdateView(UpdateView):
    model = Library_Category
    form_class = LibraryCategoryForm
    template_name = 'other_app/library_cat/create_update.html'
    success_url = reverse_lazy('library_cat_list')




class Library_CategoryDeleteView(DeleteView):
    model = Library_Category
    template_name = 'other_app/library_cat/delete.html'
    success_url = reverse_lazy('library_cat_list')
    context_object_name ='library_cat' # Ma'lumot o'chirilgandan keyin qaytish joyi

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))



