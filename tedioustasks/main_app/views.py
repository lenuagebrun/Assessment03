from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import DeleteView

def home(request):
  tasks = Task.objects.all()
  task_form = TaskForm()
  if request.method == 'POST':
    task_form = TaskForm(request.POST)
    if task_form.is_valid():
      task_form.save()
  
  return render(request, 'home.html', {
    'tasks': tasks,
    'task_form': task_form,
    })

class TaskDelete(DeleteView):
  model = Task
  success_url = '/'