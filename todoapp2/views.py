from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import Todoforms
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView


# Create your views here.

class TaskListview(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'


class TaskDetailview(DetailView):
    madel = Task
    template_name = 'detail.html'
    context_object_name = 'i'


def task_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        priority = request.POST.get("priority")
        date = request.POST.get("date")
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
    obj1 = Task.objects.all()
    print(obj1)
    return render(request, 'task_view.html', {'obj1': obj1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})


def update(request, id):
    task1 = Task.objects.get(id=id)
    form = Todoforms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task1': task1, 'form': form})
