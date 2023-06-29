from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import (
    TaskForm,
    WorkerCreationForm,
    TaskSearchForm,
    WorkerSearchForm,
    PositionSearchForm,
    TaskTypeSearchForm,
)
from manager.models import Worker, Task, TaskType, Position


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "manager/index.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["num_workers"] = Worker.objects.count()
        context["num_tasks"] = Task.objects.count()
        context["num_of_done_tasks"] = Task.objects.filter(
            is_completed=True
        ).count()
        return context


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 10
    queryset = Task.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            if name is not None:
                queryset = Task.objects.filter(name__icontains=name)
            else:
                queryset = Task.objects.all()
            return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task_list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task_list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task_list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    paginate_by = 10
    queryset = Worker.objects.all()  # Specify the initial queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_form = WorkerSearchForm(data=self.request.GET or None)
        context["search_form"] = search_form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = WorkerSearchForm(data=self.request.GET)
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            if keyword:
                queryset = queryset.filter(name__icontains=keyword)
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("manager:worker_list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("manager:worker_list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:worker_list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "manager/position_list.html"
    paginate_by = 10
    queryset = Position.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        position = self.request.GET.get("position")
        context["search_form"] = PositionSearchForm(initial={"name": name})
        context["num_of_people_in_position"] = Worker.objects.filter(position=position).count()

        return context

    def get_queryset(self):
        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"
    paginate_by = 10
    queryset = TaskType.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskTypeSearchForm(initial={"name": name})

        return context

    def get_queryset(self):
        form = TaskTypeSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list.html")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list.html")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-type-list.html")
