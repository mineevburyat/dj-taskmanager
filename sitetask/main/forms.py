from django import forms
from .models import Project

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
