from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, TaskViewSet, 
    TaskAssignView, UserTasksView, TaskUpdateView
)

# DRF Router Setup
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)), 
    path('tasks/<int:task_id>/assign/', TaskAssignView.as_view(), name='task-assign'),

    path('users/<int:user_id>/tasks/', UserTasksView.as_view({'get': 'list'}), name='user-tasks'),

    path('tasks/<int:task_id>/update/', TaskUpdateView.as_view(), name='task-update'),
]
