from rest_framework.generics import ListCreateAPIView

from todo.serializers import ToDoSerializer
from todo.models import ToDo


class ToDoListCreate(ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()