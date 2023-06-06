from django.db import models
from django.contrib.auth.models import User

TASK_PRIORITY = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
]

TASK_STATUS = [
    ('active', 'Active'),
    ('done', 'Done'),
]


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=TASK_PRIORITY)
    status = models.CharField(max_length=10, choices=TASK_STATUS, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " " + self.title

