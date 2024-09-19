from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by(
        "is_completed",
        "-creation_datetime",
    )


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
