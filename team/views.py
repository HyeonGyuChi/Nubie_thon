from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Project, User

def main(request):
    project = Project.objects
    return render(request, 'team/main.html', {'project' : project})

def new(request):
    return render(request, 'team/new.html')

def create(request):
    project = Project()
    project.title = request.GET['title']
    project.body = request.GET['body']
    project.pub_date = timezone.datetime.now() 
    # project.leader = request.GET['leader']
    # project.team01 = request.GET['team01']
    # project.team02 = request.GET['team02']
    # project.team03 = request.GET['team03']
    project.leader = get_object_or_404(User, pk = 1)
    project.team01 = get_object_or_404(User, pk = 2)
    project.team02 = get_object_or_404(User, pk = 3)
    project.team03 = get_object_or_404(User, pk = 4)
    project.save()    
    return redirect('/project/'+str(project.id))

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'team/detail.html', {'project': project_detail})

def modify(request, project_id):
    project = get_object_or_404(Project, pk = project_id)    
    return render(request, 'team/modify.html', {'project':project})


def update(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    project.title = request.GET['title'] 
    project.body = request.GET['body']  
    project.save()    
    return redirect('/project/'+str(project.id))

def delete(request, project_id):        
    project = get_object_or_404(Project, pk = project_id)        
    project.delete()        
    return redirect('main')