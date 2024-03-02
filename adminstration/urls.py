from django.urls import path
from adminstration.classcrud.index import index

from adminstration.classcrud.category import CategoryListView, CategoryCreateView, \
    CategoryUpdateView, CategoryDeleteView

from adminstration.classcrud.filter import FiltersListView, FiltersCreateView, FiltersUpdateView, FilterDeleteView

from adminstration.classcrud.filter_category import FilterCategoryListView, FilterCategoryCreateView, \
    FilterCategoryUpdateView, FilterCategoryDeleteView

from adminstration.classcrud.library_cat import Library_CategoryCreateView, Library_CategoryUpdateView, \
    Library_CategoryDeleteView, Library_CategoryListView

from adminstration.classcrud.period_filter import PeriodFilterListView, \
    PeriodFilterCreateView, PeriodFilterUpdateView, PeriodFilterDeleteView

from adminstration.classcrud.library import LibraryCreateView, LibraryUpdateView, LibraryDeleteView, LibraryListView

from adminstration.classcrud.news import NewsCreateView, NewsUpdateView, NewsDeleteView, NewsListView

from adminstration.classcrud.resourse import ResourceListView, ResourceCreateView, ResourceUpdateView, \
    ResourceDeleteView, ProductCreate, ProductUpdate

from adminstration.classcrud.sliders import SliderCreateView, SliderUpdateView, SliderDeleteView, SliderListView

from adminstration.classcrud.about import AboutCreateView, AboutUpdateView, AboutDeleteView, AboutListView

from adminstration.classcrud.comment import CommentsCreateView, CommentsUpdateView, \
    CommentsDeleteView, CommentsListView

from adminstration.classcrud.connection import ConnectionCreateView, ConnectionDeleteView, ConnectionListView, \
    ConnectionUpdateView
from adminstration.classcrud.event import EventCreateView, EventUpdateView, EventDeleteView, EventListView

from adminstration.classcrud.feedback import FeedbacksCreateView, FeedbacksUpdateView, FeedbacksDeleteView, \
    FeedbacksListView

urlpatterns = [

    # path('products/', ProductList.as_view(), name='list_products'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    # path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    # path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),



    # resources url
    path('resources/', ResourceListView.as_view(), name='resources-list'),
    path('resources/create/', ResourceCreateView.as_view(), name='resources-create'),
    path('resources/<int:pk>/update/', ResourceUpdateView.as_view(), name='resources-update'),
    path('resources/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resources-delete'),

    # Category
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # period_filter url
    path('period-filters/', PeriodFilterListView.as_view(), name='period-filter-list'),
    path('period-filter/create/', PeriodFilterCreateView.as_view(), name='period-filter-create'),
    path('period-filter/<int:pk>/update/', PeriodFilterUpdateView.as_view(), name='period-filter-update'),
    path('period-filter/<int:pk>/delete/', PeriodFilterDeleteView.as_view(), name='period-filter-delete'),

    # filter_category url
    path('filter-categories/', FilterCategoryListView.as_view(), name='filter-category-list'),
    path('filter-categories/create/', FilterCategoryCreateView.as_view(), name='filter-category-create'),
    path('filter-categories/<int:pk>/update/', FilterCategoryUpdateView.as_view(), name='filter-category-update'),
    path('filter-categories/<int:pk>/delete/', FilterCategoryDeleteView.as_view(), name='filter-category-delete'),

    # filter url
    path('filters/', FiltersListView.as_view(), name='filters-list'),
    path('filters/create/', FiltersCreateView.as_view(), name='filter-create'),
    path('filters/<int:pk>/update/', FiltersUpdateView.as_view(), name='filters-update'),
    path('filters/<int:pk>/delete/', FilterDeleteView.as_view(), name='filters-delete'),

    # labrary CAT url
    path('library_cat/create/', Library_CategoryCreateView.as_view(), name='library_cat_create'),
    path('library_cat/update/<int:pk>/', Library_CategoryUpdateView.as_view(), name='library_cat_update'),
    path('library_cat/delete/<int:pk>/', Library_CategoryDeleteView.as_view(), name='library_cat_delete'),
    path('library_cat/list/', Library_CategoryListView.as_view(), name='library_cat_list'),

    # labrary url
    path('library/create/', LibraryCreateView.as_view(), name='library_create'),
    path('library/update/<int:pk>/', LibraryUpdateView.as_view(), name='library_update'),
    path('library/delete/<int:pk>/', LibraryDeleteView.as_view(), name='library_delete'),
    path('library/list/', LibraryListView.as_view(), name='library_list'),

    # news url
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/list/', NewsListView.as_view(), name='news_list'),

    # sliders url
    path('slider/create/', SliderCreateView.as_view(), name='slider_create'),
    path('slider/update/<int:pk>/', SliderUpdateView.as_view(), name='slider_update'),
    path('slider/delete/<int:pk>/', SliderDeleteView.as_view(), name='slider_delete'),
    path('slider/list/', SliderListView.as_view(), name='slider_list'),

    # events url
    path('events/create/', EventCreateView.as_view(), name='events_create'),
    path('events/update/<int:pk>/', EventUpdateView.as_view(), name='events_update'),
    path('events/delete/<int:pk>/', EventDeleteView.as_view(), name='events_delete'),
    path('events/list/', EventListView.as_view(), name='events_list'),

    # connection url
    path('connection/create/', ConnectionCreateView.as_view(), name='connection_create'),
    path('connection/update/<int:pk>/', ConnectionUpdateView.as_view(), name='connection_update'),
    path('connection/delete/<int:pk>/', ConnectionDeleteView.as_view(), name='connection_delete'),
    path('connection/list/', ConnectionListView.as_view(), name='connection_list'),

    # about url
    path('about/create/', AboutCreateView.as_view(), name='about_create'),
    path('about/update/<int:pk>/', AboutUpdateView.as_view(), name='about_update'),
    path('about/delete/<int:pk>/', AboutDeleteView.as_view(), name='about_delete'),
    path('about/list/', AboutListView.as_view(), name='about_list'),

    # feedback url
    path('feedback/create/', FeedbacksCreateView.as_view(), name='feedback_create'),
    path('feedback/update/<int:pk>/', FeedbacksUpdateView.as_view(), name='feedback_update'),
    path('feedback/delete/<int:pk>/', FeedbacksDeleteView.as_view(), name='feedback_delete'),
    path('feedback/list/', FeedbacksListView.as_view(), name='feedback_list'),

    # comment url
    path('comment/create/', CommentsCreateView.as_view(), name='comment_create'),
    path('comment/update/<int:pk>/', CommentsUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:pk>/', CommentsDeleteView.as_view(), name='comment_delete'),
    path('comment/list/', CommentsListView.as_view(), name='comment_list'),
]
