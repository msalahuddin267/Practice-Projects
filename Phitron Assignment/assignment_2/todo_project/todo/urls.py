from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('add_task/', views.add_task, name='add_task'),
    path('show_task/', views.show_task, name='show_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('completed/<int:id>', views.completed_task, name='completed'), 
]