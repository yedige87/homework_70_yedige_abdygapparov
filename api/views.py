from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import ToDoSerializer, ProjectSerializer, TypeSerializer
from webapp.models import ToDo, Project, Type


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


class ProjectsAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response({'pk': pk})



class TypesAPIView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeDetailView(generics.RetrieveAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeUpdateView(generics.UpdateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeCreateView(generics.CreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeDeleteView(generics.DestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        type = get_object_or_404(Type, pk=pk)
        type.delete()
        return Response({'pk': pk})