# Generated by Django 4.2.5 on 2023-09-08 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='parent',
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=600, verbose_name='Описание')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.task', verbose_name='родительская задача')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Задача',
            },
        ),
    ]
