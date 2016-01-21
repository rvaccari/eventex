from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscritionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = "Rodrigo Vaccari",
            cpf='12345678901',
            email='rodrigo@vaccari.net',
            phone='51-82645533'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto create_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)