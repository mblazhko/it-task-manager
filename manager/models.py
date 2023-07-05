from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True, blank=True, related_name='workers'
    )

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Worker, related_name="members")

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    STATUS_CHOICES = (
        ("working", "Working"),
        ("complete", "Complete"),
        ("canceled", "Canceled"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    team = models.ManyToManyField(Team, related_name="projects")

    class Meta:
        ordering = ("name", "status")

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("urgent", "Urgent"),
        ("critical", "Critical"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="assignees"
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ["-priority", "-deadline"]

    def __str__(self) -> str:
        return f"{self.name} ({self.priority})"
