from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:dog_pk>', views.edit, name='edit'),
    path('delete/<int:dog_pk>', views.delete, name='delete')
]