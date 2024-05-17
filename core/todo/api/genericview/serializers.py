from django.urls import reverse
from rest_framework import serializers
from todo.models import Task


class ListTaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    class Meta:
        model = Task
        fields = ['id', 'title', 'complete', 'absolute_url']
    
    def get_abs_url(self, obj):
        request = self.context.get("request")
        # return request.build_absolute_uri(obj.pk)
        return request.build_absolute_uri(reverse('api-generic:taskDetail', args=[obj.pk]))
    
    

class DetailTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'complete', 'created_date', 'updated_date']
        read_only_fields = ["user"]
