from django.urls import path
from .views import home, create_task, edit_task, delete_task, complete_task

urlpatterns = [
    path('home/', home, name="home"),
    path('create_task/', create_task, name="create_task"),
    path('edit_task/<int:id>/', edit_task, name="edit_task"),
    path('delete_task/<int:id>/', delete_task, name="delete_task"),
    path('complete_task/<int:id>/', complete_task, name="complete_task"),
]