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
        available_employees = []
        # ищем наименее загруженного сотрудника
        for emp in employees:
            list_task = emp.tasks.filter(status=0)
            emp_data[emp.pk] = len(list_task)
        min_count = min(emp_data.values())
        # if task.employee.full_name not in available_employees:
        available_employees = [
            emp.full_name for emp in employees if emp_data[emp.pk] == min_count
        ]
        # ищем подходящего сотрудника, выполняющего родительскую задачу
        for emp in employees:
            tasks = Task.objects.filter(parent=task.id)
            for t in tasks:
                if (
                        # task.parent == t.parent
                        # and len(tasks) - min_count <= 2
                        t.employee == emp and
                        emp.full_name not in available_employees
                ):
                    available_employees.append(emp.full_name)
        return available_employees


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user', )
        # validators = [
        #     RelatedRewardValidator('related_to', 'reward'),
        #     TimeDurationValidator('duration'),
        #     RelatedIsPleasantValidator('related_to'),
        #     PleasantNotRewardAndRelatedValidator(
        #         'is_pleasant',
        #         'related_to',
        #         'reward'),
        #     PeriodValidator('period'),
        # ]