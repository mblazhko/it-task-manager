from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Position

POSITION_LIST_URL = reverse("manager:position-list")
WORKER_LIST_URL = reverse("manager:worker-list")
WORKER_DETAIL_URL = reverse("manager:worker-detail", kwargs={"pk": 1})
TASK_TYPE_LIST_URL = reverse("manager:task-type-list")
TEAM_LIST_URL = reverse("manager:team-list")
PROJECT_LIST_URL = reverse("manager:project-list")
PROJECT_DETAIL_URL = reverse("manager:project-detail", kwargs={"pk": 1})
TASK_LIST_URL = reverse("manager:task-list")
TASK_DETAIL_URL = reverse("manager:task-detail", kwargs={"pk": 1})


class BasePrivateTest(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.position = Position.objects.create(name="test_position")
        self.admin_user = get_user_model().objects.create_superuser(
            username="user.admin", password="testpassword12589"
        )
        self.client.force_login(self.admin_user)

        number_of_users = 11

        for users in range(number_of_users):
            get_user_model().objects.create(
                username=f"TestUser {users}",
                password=f"tests126 {users}",
                license_number=self.position,
            )


class PublicPositionTest(TestCase):
    def test_list_login_reqired(self):
        res = self.client.get(POSITION_LIST_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_detail_login_reqired(self):
        res = self.client.get(POSITION_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class PublicWorkerTest(TestCase):
    def test_list_login_reqired(self):
        res = self.client.get(WORKER_LIST_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_detail_login_reqired(self):
        res = self.client.get(WORKER_DETAIL_URL)

        self.assertNotEqual(res.status_code, 200)

class PublicTaskTypeTest(TestCase):
    def test_list_login_reqired(self):
        res = self.client.get(TASK_TYPE_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class PublicTeamTest(TestCase):
    def test_list_login_reqired(self):
        res = self.client.get(POSITION_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class PublicProjectTest(TestCase):
    def test_list_login_reqired(self):
        res = self.client.get(PROJECT_LIST_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_detail_login_reqired(self):
        res = self.client.get(PROJECT_DETAIL_URL)

        self.assertNotEqual(res.status_code, 200)


class PublicTaskTest(TestCase):
    def test_list_login_reqired(self):
        res = self.client.get(TASK_LIST_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_list_login_reqired(self):
        res = self.client.get(TASK_DETAIL_URL)

        self.assertNotEqual(res.status_code, 200)


