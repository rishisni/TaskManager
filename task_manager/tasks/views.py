from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from .models import CustomUser, Task
from .serializers import TaskSerializer, UserSerializer

# User ViewSet (Auto CRUD: List, Retrieve, Create, Update, Delete)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Task ViewSet (Auto CRUD: List, Retrieve, Create, Update, Delete)
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Assign Task to Users
class TaskAssignView(APIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        user_ids = request.data.get('user_ids', [])

        if not user_ids:
            return Response({"error": "User IDs required"}, status=status.HTTP_400_BAD_REQUEST)

        users = CustomUser.objects.filter(id__in=user_ids)
        
        if users.count() != len(user_ids):
            return Response({"error": "One or more User IDs are invalid"}, status=status.HTTP_400_BAD_REQUEST)

        task.assigned_users.set(users)
        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)


# Get Tasks for a Specific User
class UserTasksView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")  
        if not CustomUser.objects.filter(id=user_id).exists():
            return Task.objects.none()  
        
        return Task.objects.filter(assigned_users__id=user_id)

    
# Update Tasks
class TaskUpdateView(APIView):
    http_method_names = ['patch', 'options', 'head']  

    def patch(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)

        
        if request.data.get("status") == "completed":
            if task.status == "completed":
                return Response({"message": "Task is already completed"}, status=status.HTTP_400_BAD_REQUEST)
            
            task.status = "completed"
            task.completed_at = now()
            task.save()

            return Response({
                "message": "Task marked as completed",
                "completed_at": task.completed_at,
                "assigned_users": list(task.assigned_users.values_list("id", flat=True)),
            }, status=status.HTTP_200_OK)

        
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task updated successfully"})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)