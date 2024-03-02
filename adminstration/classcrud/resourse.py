# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
#
# from adminstration.forms import ResourceForm
# from resources.models import Resourse
#
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminstration.forms import ResourceForm, ImageFormSet, VariantFormSet
from resources.models import Resource


class ResourceListView(ListView):
    model = Resource
    template_name = 'resources/resource/list.html'
    context_object_name = 'resources'


#
class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resources/resource/create_update.html'
    success_url = reverse_lazy('resources-list')


class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resources/resource/create_update.html'
    success_url = reverse_lazy('resources-list')


class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = 'resources/resource/delete.html'
    success_url = reverse_lazy('resources-list')
    context_object_name = 'resource'

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs.get('pk'))


class ProductInline():
    form_class = ResourceForm
    model = Resource
    template_name = "resources/resource/product_create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('resources-list')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.product = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving. Useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.product = self.object
            image.save()


class ProductCreate(ProductInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': VariantFormSet(prefix='variants'),
                'images': ImageFormSet(prefix='images'),
            }
        else:
            return {
                'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }


class ProductUpdate(ProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object,
                                       prefix='variants'),
            'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object,
                                   prefix='images'),
        }





# def delete_image(request, pk):
#     try:
#         image = Image.objects.get(id=pk)
#     except Image.DoesNotExist:
#         messages.success(
#             request, 'Object Does not exit'
#         )
#         return redirect('products:update_product', pk=image.product.id)
#
#     image.delete()
#     messages.success(
#         request, 'Image deleted successfully'
#     )
#     return redirect('products:update_product', pk=image.product.id)
#
#
# def delete_variant(request, pk):
#     try:
#         variant = Variant.objects.get(id=pk)
#     except Variant.DoesNotExist:
#         messages.success(
#             request, 'Object Does not exit'
#         )
#         return redirect('products:update_product', pk=variant.product.id)
#
#     variant.delete()
#     messages.success(
#         request, 'Variant deleted successfully'
#     )
#     return redirect('products:update_product', pk=variant.product.id)
