from rest_framework.response import Response
from todo.models import Task
from .serializers import ListTaskSerializer, DetailTaskSerializer
from rest_framework import permissions
from rest_framework import generics


class TodoListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ListTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # list of task - but base on user request so we can not use queryset only
        # tasks = self.queryset.filter(user= self.request.user)
        tasks = Task.objects.filter(user= request.user)
        serializer = ListTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "todo_id"

    def get_object(self, queryset=None):
        obj = Task.objects.get(pk=self.kwargs["todo_id"])
        return obj

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response({"detail": "successfully removed"})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = DetailTaskSerializer(
            data=request.data, instance=object, many=False
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
