from django.contrib import admin
from djangoIntroduction.tasks_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'done']
