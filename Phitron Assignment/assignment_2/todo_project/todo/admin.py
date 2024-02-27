from django.contrib import admin
from todo.models import TaskFieldModel

class TaskFieldModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
admin.site.register(TaskFieldModel, TaskFieldModelAdmin)