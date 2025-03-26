from rest_framework import serializers
from .models import CustomUser, Task

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'mobile', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  
        user.save()
        return user


# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users', 'assigned_user_ids']

    def create(self, validated_data):
        assigned_users = validated_data.pop('assigned_user_ids', [])
        task = Task.objects.create(**validated_data)
        task.assigned_users.set(assigned_users)
        return task

    def update(self, instance, validated_data):
        if 'assigned_user_ids' in validated_data:
            assigned_users = validated_data.pop('assigned_user_ids')
            instance.assigned_users.set(assigned_users)
        return super().update(instance, validated_data)
