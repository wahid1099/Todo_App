from django.shortcuts import render, redirect
from .models import Todo
import time

# Create your views here.


def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        time.sleep(2)
        return redirect('/')

    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')
