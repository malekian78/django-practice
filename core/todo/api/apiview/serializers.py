from rest_framework import serializers
from todo.models import Task
from accounts.models import User


class ListTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'complete', 'created_date']
    
    def create(self, validated_data):
        validated_data["user"] = User.objects.get(id=self.context.get("request").user.id)
        return super().create(validated_data)
    

class DetailTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'complete', 'created_date', 'updated_date']
        read_only_fields = ["user"]