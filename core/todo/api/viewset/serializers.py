from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id', 'user', 'title', 'complete',]
        fields = "__all__"
        read_only_fields = ["user"]