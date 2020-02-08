from django.urls import path
from . import views

# Patrons URL creats perquè se vegin al blog.

urlpatterns = [
    path('', views.post_list, name='post_list'),
]