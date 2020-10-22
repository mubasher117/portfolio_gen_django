from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),


]
