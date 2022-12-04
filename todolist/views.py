from django.shortcuts import render, redirect
from .forms import TodoForm
from django.urls import reverse
from .models import Todolist


def todo(request):
    todo_task = Todolist.objects.all().order_by('-created_at').values()
    return render(request, 'todolist/show.html', {'all_tasks': todo_task})


def add_notes(request):
    #todo_notes = Todolist(todo=request.POST.get('todo'))
    # todo_notes.save()
    # return redirect('/')

    # add the dictionary during initialization
    forms = TodoForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('/')

    context = {
        "forms": forms
    }
    return render(request, "todolist/index.html", context)


def delete(request, id):
    note = Todolist.objects.get(id=id)
    note.delete()
    return redirect('/')


def search(request, id):
    n = Todolist.objects.get(id=id)
    return render(request, 'todolist/index.html', {'n': n})


def update(request, id):
    #a = Todolist(todo=request.POST.get('todo'))
    # a.update()
    # return HttpResponseRedirect('/')

    todo = Todolist.objects.get(id=id)
        
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
             form.save()
             return redirect('/')

    context = {
     "form": form,
    }
    return render(request, "todolist/edit.html", context)
