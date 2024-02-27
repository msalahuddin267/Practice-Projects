from django.shortcuts import render, redirect
from todo.models import TaskFieldModel
from todo.forms import TaskFieldForm


# Create your views here.

def home(request):
    return render(request, 'base.html')

def add_task(request):
    if request.method == 'POST':
        task = TaskFieldForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show_task')
    else:
        task = TaskFieldForm()
        
    return render(request, 'add_task.html', {'form' : task})
            

def show_task(request):
    task = TaskFieldModel.objects.all()
    return render(request, 'show_task.html', {'data' : task})

def edit_task(request, id):
    task = TaskFieldModel.objects.get(pk=id)
    form = TaskFieldForm(instance=task)
    if request.method == 'POST':
        form = TaskFieldForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
        
    return render(request, 'add_task.html', {'form' : form})

def delete_task(request, id):
    task = TaskFieldModel.objects.get(pk=id).delete()
    return redirect('show_task')

def completed_task(request, id):
    task = TaskFieldModel.objects.get(pk=id).delete()
    return redirect('show_task')
