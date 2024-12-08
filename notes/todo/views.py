from django.shortcuts import render, redirect
from .models import *
from .forms import *


def todo_list(request):
    todo = Note.objects.all()
    return render(request, 'todo_list.html', {'todos': todo})


def create_todo(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if not form.is_valid():
            return render(request, 'create_todo.html', {'form': form})

        title = form.cleaned_data['title']
        description = form.cleaned_data['description']

        Note.objects.create(title=title, description=description)
        return redirect('todo_list')
    else:
        form = NoteForm()
        return render(request, 'create_todo.html', {'form': form})