from django.test import TestCase

from ecommerce.apps.account.models import Customer


class TestAccount(TestCase):
    def setUp(self):
        self.data = Customer.objects.create(email="a@a.com", full_name="admin", password="")

    def test_validate_email(self):
        response = self.data
        self.assertEqual(response.__str__(), "admin")
