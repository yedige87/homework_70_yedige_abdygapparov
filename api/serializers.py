from rest_framework import serializers

from django.contrib.auth.models import User

from webapp.models import ToDo, Project, Type


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
                'id', 'status', 'title', 'text', 'deadline', 'project', 'type', 'is_deleted', 'created_at', 'updated_at',
                'deleted_at')
        read_only_fields = ('id', 'is_deleted', 'created_at', 'updated_at', 'deleted_at')


class ProjectSerializer(serializers.ModelSerializer):
    todo = ToDoSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = (
            'id', 'project', 'users', 'text', 'date_start', 'date_end', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TypeSerializer(serializers.ModelSerializer):
    type = ToDoSerializer(many=True, read_only=True)
    class Meta:
        model = Type
        fields = (
            'id', 'type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')



