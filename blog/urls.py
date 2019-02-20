from django.urls import path

from blog import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('dev/', views.dev, name='dev'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),

    path('posts/', views.post_list, name='blog'),
    path('posts/<str:category_name>/', views.post_list, name='post-list'),

]
