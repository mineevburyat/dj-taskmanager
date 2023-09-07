from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse('<h1>Привет мир</h1>')

def index(request):
        return render(request, 'main/index.html', context={'request': request})