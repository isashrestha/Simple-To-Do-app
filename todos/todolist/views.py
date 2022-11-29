from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todolist


# Create your views here.
def todo(request):
    todo_task = Todolist.objects.all().order_by('-created_at').values()
    return render(request, 'todolist/index.html', {'all_tasks': todo_task})


def add_notes(request):
    todo_notes = Todolist(todo=request.POST.get('todo'))
    todo_notes.save()
    return redirect('/')


def delete(request, id):
    note = Todolist.objects.get(id=id)
    note.delete()
    return HttpResponseRedirect('/')


def search(request, id):
    n = Todolist.objects.get(id=id)
    return render(request, 'todolist/index.html', {'n': n})
