from django.test import TestCase
from django.contrib.auth.models import User
from .models import Room

# Create your tests here.


class RoomModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.room = Room.objects.create(
            name='Test Room',
            capacity=10,
            description='Test Description',
            owner=self.user,
            start_time=None,
            end_time=None,
            booking=False
        )

    def test_room_str(self):
        self.assertEqual(str(self.room), "Test Room 10 kishilik Test Description")

    def test_room_unique_name(self):
        with self.assertRaises(Exception):
            Room.objects.create(
                name='Test Room',
                capacity=5,
                description='Another Room',
                owner=self.user,
                start_time=None,
                end_time=None,
                booking=False
            )

    def test_room_booking_default_value(self):
        self.assertFalse(self.room.booking)

    def test_room_owner(self):
        self.assertEqual(self.room.owner, self.user)
