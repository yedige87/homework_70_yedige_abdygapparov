from rest_framework import serializers

from django.contrib.auth.models import User

from webapp.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
                'id', 'status', 'title', 'text', 'deadline', 'project', 'type', 'is_deleted', 'created_at', 'updated_at',
                'deleted_at')
        read_only_fields = ('id', 'is_deleted', 'created_at', 'updated_at', 'deleted_at')

