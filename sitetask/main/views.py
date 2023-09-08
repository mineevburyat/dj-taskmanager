from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.
def about(request):
    template = 'main/about.html'
    return render(
        request,
        template_name=template,
        context={})

def index(request):
    template = 'main/index.html'
    context = {
        'projects': Project.objects.all()
    }
    return render(request, template, context=context)

def create(request):
    error = None
    if request.method == "POST":
        form = ProjectForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            error = 'ошибка в форме'
    template = 'main/create_project.html'
    context = {
        'form': ProjectForm(),
        'error': error
    }
    return render(request, template, context=context)