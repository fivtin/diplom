from django.contrib import admin

from tasks.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'employee', 'deadline', 'status', 'parent', 'user', )
    list_filter = ('status', 'user', 'employee', )
    search_fields = ('title', )
