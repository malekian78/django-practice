from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'user', 'complete', 'created_date', 'updated_date']
    ordering = ['-created_date']

admin.site.register(Task, TaskAdmin)