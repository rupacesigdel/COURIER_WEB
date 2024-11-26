from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.core.exceptions import ValidationError
from enum import Enum
from django.conf import settings


class CustomerManager(models.Manager):
    """Custom manager to filter customer users."""
    def get_queryset(self):
        return super().get_queryset().filter(is_customer=True)


class DeliveryAgentManager(models.Manager):
    """Custom manager to filter delivery agent users."""
    def get_queryset(self):
        return super().get_queryset().filter(is_delivery_agent=True)


class User(AbstractUser):
    """Custom User model."""
    is_customer = models.BooleanField(default=False)
    is_delivery_agent = models.BooleanField(default=False)

    # Custom managers
    customers = CustomerManager()
    delivery_agents = DeliveryAgentManager()


class OrderStatus(Enum):
    """Enum for order statuses."""
    PENDING = 'Pending'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'

    @classmethod
    def choices(cls):
        """Returns choices for the status field."""
        return [(tag.value, tag.value) for tag in cls]


class Order(models.Model):
    """Model for courier orders."""
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="customer_orders"
    )
    delivery_agent = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_deliveries"
    )
    pickup_address = models.TextField()
    dropoff_address = models.TextField()
    item_description = models.TextField()
    weight = models.FloatField()
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices(),
        default=OrderStatus.PENDING.value
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def assign_agent(self, agent):
        """Assign a delivery agent to the order."""
        if not agent.is_delivery_agent:
            raise ValueError("Assigned user is not a delivery agent.")
        self.delivery_agent = agent
        self.save()

    def estimated_delivery_time(self):
        """Estimate delivery time based on weight."""
        return self.created_at + timedelta(hours=self.weight * 0.5)

    def clean(self):
        """Validate order fields."""
        if self.weight <= 0:
            raise ValidationError("Weight must be greater than zero.")
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    delivery_address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"

class Pickup(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='pickup')
    pickup_address = models.TextField()
    pickup_time = models.DateTimeField()
    is_pickup_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Pickup for Booking {self.booking.id}"


class CustomsClearanceExport(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='export_clearance')
    clearance_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Rejected', 'Rejected')], default='Pending')
    export_documentation = models.TextField(help_text="List of required export documents")
    customs_officer_name = models.CharField(max_length=100, null=True, blank=True)
    clearance_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Export Customs Clearance for Booking {self.booking.id} - Status: {self.clearance_status}"

class CustomsClearanceImport(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='import_clearance')
    clearance_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Rejected', 'Rejected')], default='Pending')
    import_documentation = models.TextField(help_text="List of required import documents")
    customs_officer_name = models.CharField(max_length=100, null=True, blank=True)
    clearance_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Import Customs Clearance for Booking {self.booking.id} - Status: {self.clearance_status}"


class LastMileDelivery(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='last_mile_delivery')
    courier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=50, choices=[('In Transit', 'In Transit'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], default='In Transit')
    estimated_delivery_time = models.DateTimeField(null=True, blank=True)
    delivery_address = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=100, unique=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Delivery Status for Booking {self.booking.id} - {self.delivery_status}"
