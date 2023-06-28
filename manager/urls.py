from django.urls import path

from manager.views import IndexView, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view, name="tasks-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view, name="tasks-detail"),
    path("tasks/create", TaskCreateView.as_view, name="tasks-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view, name="tasks-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view, name="tasks-delete"),

]