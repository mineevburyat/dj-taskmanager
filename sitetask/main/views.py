from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.views.generic import DetailView, CreateView

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

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'main/detail_project.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(project=self.object.id)
        return context
    
class CreateTaskView(CreateView):
    form_class = TaskForm
    template_name = 'main/addtask.html'
    
    # fields = ['title', 'description', 'project']
    model = Task
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_project = self.kwargs.get('pk')
        project = Project.objects.get(pk=pk_project)
        context['project'] = project
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.project = Project.objects.get(id=self.kwargs.get('pk'))
        self.object.save()
        return super(CreateTaskView, self).form_valid(form)
    
    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('main:detail', kwargs={'pk': pk})