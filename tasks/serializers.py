from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employees.models import Employee
from tasks.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskImportantSerializer(ModelSerializer):
    tasks = TaskSerializer(source='children', many=True)
    available_employees = SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_available_employees(self, task):
        employees = Employee.objects.all()
        emp_data = {}
        for emp in employees:
            list_task = emp.tasks.filter(status=0)
            emp_data[emp.pk] = len(list_task)
        min_count = min(emp_data.values())
        available_employees = [
            emp.full_name for emp in employees if emp_data[emp.pk] == min_count
        ]
        for emp in employees:
            tasks = Task.objects.filter(parent=task.id)
            for t in tasks:
                if t.employee == emp and emp.full_name not in available_employees:
                    available_employees.append(emp.full_name)
        return available_employees


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user', )
