# from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import inlineformset_factory


from other_app.models import Library_Category, Library, Sliders, News, Event, Connection, About, Feedbacks, Comments
from resources.models import Category, PeriodFilter, FilterCategories, Filters, Resource, Attributes, Contents


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'icon', 'order', 'interactive')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'id': "title",
                       "placeholder": "Title name"}
            ),
            'icon': forms.TextInput(
                attrs={'class': 'form-control', 'id': "icon",
                       "placeholder": "Icon name"}
            ),
            'order': forms.NumberInput(
                attrs={'class': 'form-control', 'id': "order",
                       "placeholder": "Icon name"}
            ),
            'interactive': forms.CheckboxInput(
                attrs={'class': 'form-control', 'id': "interactive",
                       "placeholder": "Interactive name"}
            ),
        }
        # labels = {
        #     'title': 'Category Title',
        #     'icon': 'Category Icon',
        #     'order': 'Category Order',
        #     'interactive': 'Interactive Category',
        # }


class PeriodFilterForm(forms.ModelForm):
    class Meta:
        model = PeriodFilter
        fields = ['title']
        labels = {
            'title': 'Sarlavha',  # Leibelni o'zgartirish
        }
        widgets = {
            'title': CKEditorWidget(),  # Widgetni o'zgartirish
        }


class FilterCategoryForm(forms.ModelForm):
    class Meta:
        model = FilterCategories
        fields = ['category', 'title']
        labels = {
            'category': 'Kategoriya',  # Kategoriya maydoni uchun leibelni o'zgartirish
            'title': 'Sarlavha',  # Sarlavha maydoni uchun leibelni o'zgartirish
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),  # Kategoriya maydoni uchun widgetni o'zgartirish
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Sarlavha maydoni uchun widgetni o'zgartirish
        }


class FiltersForm(forms.ModelForm):
    class Meta:
        model = Filters
        fields = ['filter_category', 'title']
        labels = {
            'filter_category': 'Filter kategoriya',  # Filter kategoriyasi maydoni uchun leibelni o'zgartirish
            'title': 'Sarlavha',  # Sarlavha maydoni uchun leibelni o'zgartirish
        }
        widgets = {
            'filter_category': forms.Select(attrs={'class': 'form-control'}),
            # Filter kategoriyasi maydoni uchun widgetni o'zgartirish
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Sarlavha maydoni uchun widgetni o'zgartirish
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['category', 'filter_category', 'filters', 'period_filter',
                  'title', 'image', 'content', 'statehood', 'province',
                  'interive_content', 'interive_title', 'interive_file']
        labels = {
            'category': 'Kategoriya',
            'filter_category': 'Filter kategoriya',
            'filters': 'Filtrlar',
            'period_filter': 'Davrli filtrlar',
            'title': 'Sarlavha',
            'image': 'Rasm',
            'content': 'Mundarija',
            'statehood': 'Holat',
            'province': 'Viloyat',
            'interive_content': 'Interaktiv Tarkibi',
            'interive_title': 'Interaktiv Sarlavha',
            'interive_file': 'Interaktiv Fayl',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'filter_category': forms.Select(attrs={'class': 'form-control'}),
            'filters': forms.Select(attrs={'class': 'form-control'}),
            'period_filter': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'statehood': forms.CheckboxInput(),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'interive_content': forms.TextInput(attrs={'class': 'form-control'}),
            'interive_title': forms.TextInput(attrs={'class': 'form-control'}),
            'interive_file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Attributes
        fields = '__all__'
        widgets = {
            'attributes_title': forms.TextInput(attrs={'class': 'form-control'}),
            'attributes_description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VariantForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = '__all__'
        widgets = {
            'contents_title': forms.TextInput(attrs={'class': 'form-control'}),
            'contents_description': forms.TextInput(attrs={'class': 'form-control'}),
        }


VariantFormSet = inlineformset_factory(
    Resource, Attributes, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
ImageFormSet = inlineformset_factory(
    Resource, Contents, form=ImageForm,
    extra=1, can_delete=True, can_delete_extra=True
)


# Library
class LibraryCategoryForm(forms.ModelForm):
    class Meta:
        model = Library_Category
        fields = ['title']
        labels = {
            'title': 'Sarlavha',  # Titlega oid label
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Titlega oid widget
        }


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['title', 'category', 'author', 'type', 'year', 'country', 'language', 'image', 'file', ]
        labels = {
            'title': 'Title:',
            'category': 'Category:',
            'author': 'Author:',
            'type': 'Type:',
            'year': 'Year:',
            'country': 'Country:',
            'language': 'Language:',
            'image': 'Image:',
            'file': 'File:',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),

        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'file', ]
        labels = {
            'title': 'Title',
            'content': 'Content',
            'file': 'File',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(),  # CKEditor widget
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),

        }


class SlidersForm(forms.ModelForm):
    class Meta:
        model = Sliders
        fields = ['title', 'file', 'link']
        labels = {
            'title': 'Title:',
            'file': 'File:',
            'link': 'Link:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'content', 'image', ]
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(),  # CKEditor widget
            'image': forms.FileInput(attrs={'class': 'form-control-image'}),

        }


class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['phone', 'phone_two', 'address', 'location', 'email', 'map']
        labels = {
            'phone': 'Telefon raqami',
            'phone_two': 'Ikkinchi telefon raqami',
            'address': 'Manzil',
            'location': 'Joylashuvi',
            'email': 'Elektron pochta',
            'map': 'Xarita'
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_two': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'map': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'content']
        labels = {
            'title': 'Sarlavha',
            'content': 'Tarkibi'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            # CKEditorWidget(config_name='awesome_ckeditor'),  # CKEditorWidget()  # CKEditorWidget-ni foydalanuvchi-interfeyssi shakli sifatida ishlatish
        }


class FeedbacksForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['message', ]
        labels = {
            'message': 'message'
        }
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'})
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['message', ]
        labels = {
            'message': 'message'
        }
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'})
        }
