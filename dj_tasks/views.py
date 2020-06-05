# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Task,
	TaskRun,
)


class TaskCreateView(CreateView):

    model = Task


class TaskDeleteView(DeleteView):

    model = Task


class TaskDetailView(DetailView):

    model = Task


class TaskUpdateView(UpdateView):

    model = Task


class TaskListView(ListView):

    model = Task


class TaskRunCreateView(CreateView):

    model = TaskRun


class TaskRunDeleteView(DeleteView):

    model = TaskRun


class TaskRunDetailView(DetailView):

    model = TaskRun


class TaskRunUpdateView(UpdateView):

    model = TaskRun


class TaskRunListView(ListView):

    model = TaskRun

