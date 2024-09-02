from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employees.models import Employee
from tasks.models import Task
from tasks.serializers import TaskSerializer


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# class EmployeeCreateSerializer(ModelSerializer):
#     class Meta:
#         model = Employee
#         exclude = ('user', )
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


class EmployeeTaskSerializer(ModelSerializer):
    # tasks = SerializerMethodField(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    active_tasks_count = SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'position', 'tasks', 'active_tasks_count', )

    def get_active_tasks_count(self, obj):
        return obj.tasks.filter(status=0).count()


    # def get_tasks(self, employee):
    #     return Task.objects.filter(employee=employee, ).count()
