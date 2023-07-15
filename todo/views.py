from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Task
from .forms import TaskForm

def home(request):
    data =  Task.objects.all()
    context = {"my_data": data}
    return render(request, template_name="todo/home.html", context=context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'todo/create_task.html', {'my_form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/create_task.html', {'my_form': form})

def complete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')

def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('home')