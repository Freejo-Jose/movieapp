from django.urls import path, include
from . import views
app_name='newapp'
urlpatterns = [
    path('', views.newproj,name='newproj'),
    path('m/<int:movieid>/', views.m, name='mohan'),
    path('update/<int:id>/', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
