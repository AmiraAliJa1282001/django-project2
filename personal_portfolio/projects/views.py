from django.shortcuts import render

# Create your views here.

from projects.models import Project

def project_index(request):
    projects = Project.objects.all()# search in documentation about all function
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # search in documentation about get function
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)