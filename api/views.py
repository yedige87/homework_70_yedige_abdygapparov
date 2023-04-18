from rest_framework import generics

from api.serializers import ToDoSerializer
from webapp.models import ToDo


class TasksAPIView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DetailView(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class UpdateView(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

