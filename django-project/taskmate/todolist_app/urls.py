from django.urls import path
from todolist_app import views

urlpatterns = [
    path('todolist', views.todolist, name = 'todolist'),
    path('contact_us', views.contact, name = 'contact_us'),
    path('about_us', views.about, name = 'about_us'),

]
