from django import forms
from .models import Booking, Pickup
from .models import CustomsClearanceExport, CustomsClearanceImport
from .models import LastMileDelivery

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


class CustomsClearanceExportForm(forms.ModelForm):
    class Meta:
        model = CustomsClearanceExport
        fields = ['clearance_status', 'export_documentation', 'customs_officer_name', 'clearance_date']

class CustomsClearanceImportForm(forms.ModelForm):
    class Meta:
        model = CustomsClearanceImport
        fields = ['clearance_status', 'import_documentation', 'customs_officer_name', 'clearance_date']



class LastMileDeliveryForm(forms.ModelForm):
    class Meta:
        model = LastMileDelivery
        fields = ['courier', 'delivery_status', 'estimated_delivery_time', 'delivery_address', 'tracking_number', 'delivered_at']
