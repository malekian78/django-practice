from rest_framework import serializers
from todo.models import Task


class ListTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'complete']
    
    

class DetailTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'complete', 'created_date', 'updated_date']
        read_only_fields = ["user"]
