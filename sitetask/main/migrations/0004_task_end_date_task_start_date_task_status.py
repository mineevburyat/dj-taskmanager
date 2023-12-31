# Generated by Django 4.2.5 on 2023-09-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_project_parent_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата завершения'),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата начала'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('run', 'в работе'), ('end', 'завершена'), ('fail', 'провалилась'), ('post', 'отложено')], default='run', max_length=14, verbose_name='статус'),
        ),
    ]
