# Generated by Django 5.0.7 on 2024-09-02 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee', verbose_name='performer'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
