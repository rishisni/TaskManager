from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

# Customizing the User Admin Panel
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'mobile', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'mobile')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('mobile',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

# Register Task Model in Admin Panel
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created_at', 'task_type', 'completed_at')
    search_fields = ('name', 'status')
    list_filter = ('status', 'task_type')
    ordering = ('-created_at',)
    filter_horizontal = ('assigned_users',)  

# Register models in the admin panel
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
