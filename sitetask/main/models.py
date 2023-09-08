from django.db import models
from django.utils.timezone import now
# Create your models here.
class Status(models.TextChoices):
    RUN = ('run', 'в работе')
    END = ('end', 'завершена')
    FAIL = ('fail', 'провалилась')
    POST = ('post', 'отложено')

class Project(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=600
    )
    
    class Meta:
        verbose_name = 'Проект'
        
    def __str__(self):
        return self.title
    
    def get_all_tasks_count(self):
        return self.tasks.all().count()
    get_all_tasks_count.short_description = "всего задач"
    
    def get_run_tasks_count(self):
        return self.tasks.filter(status=Status.RUN).count()
    get_run_tasks_count.short_description = "задач в работе"
    
    def get_end_tasks_count(self):
        return self.tasks.filter(status=Status.END).count()
    get_run_tasks_count.short_description = "задач выполнено"
    
    def get_fail_tasks_count(self):
        return self.tasks.filter(status__in = (Status.FAIL, Status.POST)).count()
    get_run_tasks_count.short_description = "задач загубленных"

    
class Task(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=600
    )
    parent = models.ForeignKey(
        "self", 
        verbose_name="родительская задача",
        on_delete=models.CASCADE, 
        null=True, 
        blank=True)
    project = models.ForeignKey(
        Project,
        verbose_name="Проект",
        related_name='tasks',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        verbose_name='статус',
        max_length=14,
        choices=Status.choices,
        default=Status.RUN)
    start_date = models.DateField(
        'дата начала',
        auto_now_add=True,
    )
    end_date = models.DateField(
        'дата завершения',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Задача'
        
    def __str__(self):
        return self.title