from rest_framework import serializers
from todo.models import Task
from rest_framework.reverse import reverse


class TaskSerializer(serializers.ModelSerializer):
    relative_url = serializers.URLField(source="get_relative_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    user = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'complete', 'created_date', 'updated_date','relative_url',
            'absolute_url',]
        read_only_fields = ['user']

    def get_abs_url(self, obj):
        request = self.context.get("request")
        # return request.build_absolute_uri(obj.pk)
        return request.build_absolute_uri(reverse('api-viewset:tasks-detail', args=[obj.pk]))

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("created_date", None)
            rep.pop("updated_date", None)
            rep.pop("user", None)
        return rep