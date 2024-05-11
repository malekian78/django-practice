from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from todo.api.viewset.permissions import IsOwnerOrReadOnly
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status


class TodoListView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [ IsOwnerOrReadOnly]

    def list(self, request):
        # getting List of Tasks
        queryset = Task.objects.filter(user= request.user)
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # def get_queryset(self, *args, **kwargs):
    #     return (
    #         super()
    #         .get_queryset(*args, **kwargs)
    #         .filter(user=self.request.user)
    #     )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_object(self, queryset=None):
        # get task base on user-Request and task-id
        obj = get_object_or_404(Task, pk=self.kwargs["pk"], user = self.request.user)
        return obj

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response({"detail": "successfully removed"})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# class TodoDetailApiView(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = "todo_id"

#     def get_object(self, queryset=None):
#         # get task base on user-Request and task-id
        
#         # obj = Task.objects.get(pk=self.kwargs["todo_id"], user = self.request.user)
#         obj = get_object_or_404(Task, pk=self.kwargs["todo_id"], user = self.request.user)
#         return obj

#     def delete(self, request, *args, **kwargs):
#         object = self.get_object()
#         object.delete()
#         return Response({"detail": "successfully removed"})

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)

#     # def post(self, request, *args, **kwargs):
#     #     object = self.get_object()
#     #     serializer = TaskSerializer(
#     #         data=request.data, instance=object, many=False
#     #     )
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #     return Response(serializer.data)
