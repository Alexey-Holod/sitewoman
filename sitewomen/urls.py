"""
URL configuration for sitewomen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter
from women.views import *
from women import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', index),
    path('cats/<int:cat_id>/', categories),
    path('cats/<slug:cat_slug>/', categories_by_slug),
    path('archive/<year4:year>', archive),
]
