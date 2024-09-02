from django.db import models

# Create your models here.


class Employee(models.Model):

    full_name = models.CharField(max_length=256, verbose_name='full name')
    position = models.CharField(max_length=128, verbose_name='position')

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return f'{self.full_name} [{self.position}]'