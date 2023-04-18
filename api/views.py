from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

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


class CreateView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()
        return Response({'pk': pk})