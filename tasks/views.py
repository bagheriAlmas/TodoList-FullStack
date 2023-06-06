from rest_framework import viewsets
from rest_framework import permissions
from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
