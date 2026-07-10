from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from .models import Table


class TablesViewTests(TestCase):
    def test_tables_view_renders_for_waiter(self):
        user = User.objects.create_user(
            username="waiter",
            password="password123",
            role=User.Role.WAITER,
        )
        table = Table.objects.create(name="Table 1")

        self.client.force_login(user)
        response = self.client.get(reverse("tables_view_url"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, table.name)
