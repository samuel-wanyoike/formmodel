from django.test import TestCase
from datetime import datetime
from .models import Logger
# Create your tests here.

class ReservationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.reservation = Logger.objects.create(
            first_name = "John",
            last_name = "McDonald"
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)

        self.assertIsInstance(self.reservation.last_name, str)
    
    def test_timestamps(self):
        self.assertIsInstance(self.reservation.time_log, datetime)