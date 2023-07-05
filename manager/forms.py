from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q, QuerySet

from manager.models import Worker, Task, Position, Project, Team


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name",
        )


class ProjectCreationForm(forms.ModelForm):
    team = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Project
        fields = "__all__"


class TeamCreationForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Team
        fields = "__all__"


class WorkerSearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Are you looking for somebody?"}
        ),
    )

    def search(self) -> QuerySet:
        keyword = self.cleaned_data.get("keyword")

        workers = Worker.objects.all()

        if keyword:
            workers = workers.filter(
                Q(username__icontains=keyword)
                | Q(first_name__icontains=keyword)
                | Q(last_name__icontains=keyword)
            )

        return workers


class TaskSearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Looking for task?"}),
    )

    def search(self) -> QuerySet:
        name = self.cleaned_data.get("name")

        tasks = Task.objects.all()

        if name:
            tasks = tasks.filter(name=name)

        return tasks


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Looking for position?"}),
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Looking for task type?"}
        ),
    )
