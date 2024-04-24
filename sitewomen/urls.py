from django.contrib import admin
from django.urls import path, include, register_converter
from women.views import *
from women import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', include('women.urls')),
    path('cats/<int:cat_id>/', categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
    path('archive/<year4:year>/', archive, name='archive'),
]

handler404 = page_not_found
