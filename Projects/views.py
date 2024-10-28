from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# Create your views here./
def Projects(request):
    projects = Project.objects.all()
    context = {"Projects": projects}
    return render(request, "Projects/Projects.html", context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    return render(request, "Projects/single_project.html", {"Project": projectobj})


def CreateProject(request):
    form = ProjectForm()  
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Projects")  
    context = {"form": form}
    return render(
        request, "Projects/Project_form.html", context
    )


def UpdateProject(request,pk):
    update=Project.objects.get(id=pk)
    form=ProjectForm(instance=update)
    if request.method=='POST':
        form=ProjectForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return redirect('Projects')
    context={'form':form}
    return render(request, "Projects/Project_form.html", context) 
    
def DeleteProject(request,pk):
    pro=Project.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('Projects')
    context={'object':project}
    return render(request,'Projects/delete_templates.html',context)