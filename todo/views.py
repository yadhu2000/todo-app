from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Heading, TodoItem
from .forms import HeadingForm, TodoForm


@login_required
def dashboard(request):
    headings = Heading.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'headings': headings})


@login_required
def heading_create(request):
    if request.method == 'POST':
        form = HeadingForm(request.POST)
        if form.is_valid():
            heading = form.save(commit=False)
            heading.user = request.user
            heading.save()
            return redirect('dashboard')
    else:
        form = HeadingForm()

    return render(request, 'heading_form.html', {'form': form})


@login_required
def heading_detail(request, id):
    heading = get_object_or_404(Heading, id=id, user=request.user)
    items = heading.items.all()
    return render(request, 'heading_detail.html', {'heading': heading, 'items': items})


@login_required
def heading_delete(request, id):
    heading = get_object_or_404(Heading, id=id, user=request.user)
    heading.delete()
    return redirect('dashboard')


@login_required
def todo_create(request, heading_id):
    heading = get_object_or_404(Heading, id=heading_id, user=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.heading = heading
            todo.save()
            return redirect('heading_detail', id=heading_id)
    else:
        form = TodoForm()

    return render(request, 'todo_form.html', {'form': form})


@login_required
def todo_edit(request, id):
    todo = get_object_or_404(TodoItem, id=id, heading__user=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('heading_detail', id=todo.heading.id)
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo_form.html', {'form': form})


@login_required
def todo_delete(request, id):
    todo = get_object_or_404(TodoItem, id=id, heading__user=request.user)
    heading_id = todo.heading.id
    todo.delete()
    return redirect('heading_detail', id=heading_id)


@login_required
def todo_complete(request, id):
    todo = get_object_or_404(TodoItem, id=id, heading__user=request.user)
    todo.completed = True
    todo.save()
    return redirect('heading_detail', id=todo.heading.id)
