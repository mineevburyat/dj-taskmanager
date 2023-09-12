from django.contrib import admin
from .models import Project, Task


class TaskInline(admin.StackedInline):
    model = Task
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]
    list_display = ("title", "get_all_tasks_count", "get_run_tasks_count")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass