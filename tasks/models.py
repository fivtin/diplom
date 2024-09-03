from django.db import models

from config import NULLABLE
from employees.models import Employee
from users.models import User


# Create your models here.

class Task(models.Model):
    """Implementation of the task model."""

    STATUS_ACTIVE = 0
    STATUS_DONE = 1

    JOB_STATUS_CHOICES = {
        STATUS_ACTIVE: "Active",
        STATUS_DONE: "Done"
    }

    title = models.CharField(max_length=256, verbose_name='title')

    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, **NULLABLE, verbose_name='performer', related_name='tasks')

    deadline = models.DateField(**NULLABLE, verbose_name='deadline')

    status = models.PositiveSmallIntegerField(default=STATUS_ACTIVE, choices=JOB_STATUS_CHOICES, verbose_name='status')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='parent task', related_name='children')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='creator')

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f'{self.title} ({self.JOB_STATUS_CHOICES[self.status]})'
