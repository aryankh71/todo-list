from django.urls import path
from .views import todo_list, create_todo

urlpatterns = [
    path('todo_list/', todo_list, name='todo_list'),
    path('create_todo/', create_todo, name='create_todo'),

]
