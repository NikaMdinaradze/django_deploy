from django.urls import path

from todo.views import ToDoListCreate

urlpatterns = [
    path("", ToDoListCreate.as_view())
]