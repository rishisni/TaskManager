from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username

# Task Model
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=100, blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(CustomUser, related_name="tasks")

    def __str__(self):
        return self.name
