from django.contrib import admin

from employees.models import Employee


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', )
    search_fields = ('full_name', )
