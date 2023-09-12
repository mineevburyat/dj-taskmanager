from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "введите название проекта",
                'class' : "form-control"}),
            'description': forms.Textarea(attrs={
                'placeholder': "введите описание проекта",
                'class' : "form-control"})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "введите название задачи",
                'class' : "form-control"}),
            'description': forms.Textarea(attrs={
                'placeholder': "введите описание задачи",
                'class' : "form-control"})
        }