from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.forms import TaskForm, TaskSearchForm
from manager.models import Team, Project, TaskType, Task, Position


class BaseFormTest(TestCase):
    def setUp(self):
        super().setUp()
        self.admin_user = get_user_model().objects.create_superuser(
            username="TestAdmin",
            password="testpass12345",
        )
        self.client.force_login(self.admin_user)

        self.team = Team.objects.create(
            name="TestTeam",
        )
        self.team.members.set([self.admin_user])

        self.project = Project.objects.create(
            name="TestProject",
            status="working",
        )
        self.project.team.set([self.team])

        self.task_type = TaskType.objects.create(
            name="TestTaskType"
        )

        self.task = Task.objects.create(
            name="test_task",
            deadline="2031-01-01",
            is_completed=False,
            priority="medium",
            task_type=self.task_type,
            project=self.project
        )
        self.task.assignees.set([self.admin_user])

        self.position = Position.objects.create(
            name="test_position",
        )


class TaskFormTest(BaseFormTest):
    def test_task_creation_form_with_non_valid_completed_status(self):
        form_data = {
            "name": "TestTask",
            "deadline": "2023-03-03",
            "is_completed": True,
            "priority": "low",
            "task_type": self.task_type.id,
            "assignees": [self.admin_user.id],
            "project": self.project.id,
        }

        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_search(self):
        form_data = {"keyword": "test"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


