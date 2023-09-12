from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='detail'),
    path('addtask/<int:pk>', views.CreateTaskView.as_view(), name='addtask'),
]