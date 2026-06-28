from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_cocheras, name='list_cocheras'),
    path('crear/', views.crear_cochera, name='crear_cochera'),
    path('editar/<int:id>', views.editar_cochera, name='editar_cochera'),
    path('liberar/<int:id>', views.liberar_cochera, name='liberar_cochera'),
    path('eliminar/<int:id>/', views.eliminar_cochera, name='eliminar_cochera'),

]