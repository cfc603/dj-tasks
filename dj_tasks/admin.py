# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Task, TaskRun


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskRun)
class TaskRunAdmin(admin.ModelAdmin):
    pass
