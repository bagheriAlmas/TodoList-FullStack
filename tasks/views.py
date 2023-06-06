from rest_framework import viewsets
from rest_framework import permissions
from .models import Task
from .serializers import TaskSerializer

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)