from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [

    path("", views.todo, name='todo'),
    path('add_notes/', views.add_notes, name='add_notes'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('search/<int:id>/', views.search, name='search'),
    path('update/<int:id>/', views.update, name='update'),
]
