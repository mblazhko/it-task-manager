from django.urls import path

from manager.views import (
    IndexView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView, ProjectDetailView, ProjectListView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("team/", WorkerListView.as_view(), name="team-list"),
    path(
        "employee/<int:pk>", WorkerDetailView.as_view(), name="employee-detail"
    ),
    path("employee/create", WorkerCreateView.as_view(), name="employee-create"),
    path(
        "employee/<int:pk>/update",
        WorkerUpdateView.as_view(),
        name="employee-update",
    ),
    path(
        "employee/<int:pk>/delete",
        WorkerDeleteView.as_view(),
        name="employee-delete",
    ),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path(
        "position/create", PositionCreateView.as_view(), name="position-create"
    ),
    path(
        "position/<int:pk>/update",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "position/<int:pk>/delete",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path(
        "task-type/create", TaskTypeCreateView.as_view(), name="task-type-create"
    ),
    path(
        "task-type/<int:pk>/update",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task-type/<int:pk>/delete",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    path(
        "projects/",
        ProjectListView.as_view(),
        name="project-list"
    ),
    path(
        "project/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail"
    )
]

app_name = "manager"
