# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.models import Task
from .serializers import ListTaskSerializer, DetailTaskSerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404
# from accounts.models import User

# List of Task api
class TodoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListTaskSerializer

    def get(self, request, *args, **kwargs):
        # Return the list of Tasks from requested user
        todos = Task.objects.filter(user=request.user.id)
        serializer = self.serializer_class(todos, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        # Create new Task 
        # ___________________________________ 
        # try to send user here but not work 
        # - maybe because i dont set 'user' in fields but even by that
        # it should be readOnly field so we can not send user here to serializer - maybe not safe too
        # data = {
        #     "title": request.data.get("title"),
        #     # "user": User.objects.get(id=request.user.id) #! not Work 
        #     "complete":  request.data.get("complete"),
        # }
        serializer = self.serializer_class(
            data= request.data, #! or could use  data  at line 24 but is same as request.data
            context= {'request': request} #! we need this line for self.context.get("request") in serializer work
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Deatil of task
class TodoDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetailTaskSerializer

    def get(self, request, todo_id, *args, **kwargs):
        # return the task with full detail of it by todo_id and user_id
        task = get_object_or_404(Task, pk=todo_id, user=request.user.id)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def put(self, request, todo_id, *args, **kwargs):
        # Edit the task
        task = get_object_or_404(Task, pk=todo_id, user=request.user)
        serializer = self.serializer_class(task, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, todo_id, *args, **kwargs):
        # Delete the task by id and user_id  
        task = get_object_or_404(Task, pk=todo_id, user=request.user.id)
        task.delete()
        return Response({'detail':'task removed successfully.'}, status=status.HTTP_200_OK)