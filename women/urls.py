from django.contrib import admin
from django.urls import path
from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', show_post, name='post')
]
