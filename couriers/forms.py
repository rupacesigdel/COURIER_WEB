from django import forms
from .models import Booking, Pickup

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 'delivery_address']

class PickupForm(forms.ModelForm):
    class Meta:
        model = Pickup
        fields = ['pickup_address', 'pickup_time']

class SortingForm(forms.Form):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('fragile', 'Fragile Items'),
    ]
    
    item_category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Select Item Category')
    destination = forms.CharField(max_length=255, label='Destination')