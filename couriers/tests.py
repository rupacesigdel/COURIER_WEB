from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='customer1', password='testpassword')
        self.order = Order.objects.create(
            customer=self.user,
            pickup_address='123 Pickup Street',
            dropoff_address='456 Dropoff Street',
            item_description='A small package',
            weight=2.5,
            status='Pending',
            price=20.00
        )

    def test_order_creation(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(self.order.customer.username, 'customer1')
