# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'dj_tasks'
urlpatterns = [
    url(
        regex="^Task/~create/$",
        view=views.TaskCreateView.as_view(),
        name='Task_create',
    ),
    url(
        regex="^Task/(?P<pk>\d+)/~delete/$",
        view=views.TaskDeleteView.as_view(),
        name='Task_delete',
    ),
    url(
        regex="^Task/(?P<pk>\d+)/$",
        view=views.TaskDetailView.as_view(),
        name='Task_detail',
    ),
    url(
        regex="^Task/(?P<pk>\d+)/~update/$",
        view=views.TaskUpdateView.as_view(),
        name='Task_update',
    ),
    url(
        regex="^Task/$",
        view=views.TaskListView.as_view(),
        name='Task_list',
    ),
	url(
        regex="^TaskRun/~create/$",
        view=views.TaskRunCreateView.as_view(),
        name='TaskRun_create',
    ),
    url(
        regex="^TaskRun/(?P<pk>\d+)/~delete/$",
        view=views.TaskRunDeleteView.as_view(),
        name='TaskRun_delete',
    ),
    url(
        regex="^TaskRun/(?P<pk>\d+)/$",
        view=views.TaskRunDetailView.as_view(),
        name='TaskRun_detail',
    ),
    url(
        regex="^TaskRun/(?P<pk>\d+)/~update/$",
        view=views.TaskRunUpdateView.as_view(),
        name='TaskRun_update',
    ),
    url(
        regex="^TaskRun/$",
        view=views.TaskRunListView.as_view(),
        name='TaskRun_list',
    ),
	]
