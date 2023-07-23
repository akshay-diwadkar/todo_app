from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
# Create your views here.
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    data =  Task.objects.all()
    context = {"my_data": data}
    return render(request, template_name="todo/home.html", context=context)

@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all posts, or create a new posts.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def get_task(request):
    print(request.data['data'])
    task = Task.objects.filter(Q(title__icontains=request.data['data']))
    print(task[0].description)
    serializer = TaskSerializer(data = {
        "title" : task[0].title,
        "description" : task[0].description,
        "start_date" : task[0].start_date,
        "end_date" :  task[0].end_date,
        "user" :  task[0].user,
        "is_completed" : task[0].is_completed,
    })
    print("comes till here")
    if serializer.is_valid():
        print("enters here?")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    return render(request, 'todo/edit_task.html', {'my_form': form})

def complete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')

def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('home')