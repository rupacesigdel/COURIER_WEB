from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.exceptions import PermissionDenied
from .models import Booking, Pickup
from .forms import BookingForm, PickupForm
from django.http import HttpResponse
from .forms import SortingForm  
from django.contrib import messages
from .forms import CustomsClearanceExportForm, CustomsClearanceImportForm
from .models import Booking, CustomsClearanceExport, CustomsClearanceImport
from .forms import LastMileDeliveryForm
from .models import LastMileDelivery, Booking

class OrderListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        if not self.request.user.is_customer:
            raise PermissionDenied("Only customers can view their orders.")
        return Order.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_customer:
            raise PermissionDenied("Only customers can create orders.")
        serializer.save(customer=self.request.user)


class OrderDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):
        order = super().get_object()
        if (
            self.request.user != order.customer
            and self.request.user != order.delivery_agent
        ):
            raise PermissionDenied("You do not have permission to access this order.")
        return order

    def perform_update(self, serializer):
        if self.request.user.is_delivery_agent:
            serializer.save(status=self.request.data.get('status', serializer.instance.status))
        elif self.request.user == serializer.instance.customer:
            serializer.save()
        else:
            raise PermissionDenied("You cannot update this order.")



def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, 'Your booking has been created successfully!')
            return redirect('booking_detail', booking_id=booking.id)
        else:
            messages.error(request, 'There was an error with your booking submission.')
    else:
        form = BookingForm()
    return render(request, 'couriers/create_booking.html', {'form': form})



def booking_detail(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    pickup_form = PickupForm()
    return render(request, 'couriers/booking_detail.html', {
        'booking': booking,
        'pickup_form': pickup_form,
    })



def create_pickup(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
            pickup = form.save(commit=False)
            pickup.booking = booking
            pickup.save()
            return redirect('pickup_detail', pickup_id=pickup.id)
    else:
        form = PickupForm()
    return render(request, 'couriers/create_pickup.html', {'form': form, 'booking': booking})


def pickup_detail(request, pickup_id):
    pickup = Pickup.objects.get(id=pickup_id)
    return render(request, 'couriers/pickup_detail.html', {'pickup': pickup})




def sorting_hub(request):
    if request.method == 'POST':
        form = SortingForm(request.POST)
        if form.is_valid():
            item_category = form.cleaned_data['item_category']
            destination = form.cleaned_data['destination']
            request.session['sorted_items'] = {'category': item_category, 'destination': destination}
            return redirect('sorting_hub')
    else:
        form = SortingForm()

    return render(request, 'couriers/sorting_hub.html', {'form': form})

def sort_items(request):
    sorted_items = request.session.get('sorted_items', [])
    return HttpResponse(f'Sorted Items: {sorted_items}')




def create_export_clearance(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = CustomsClearanceExportForm(request.POST)
        if form.is_valid():
            customs_clearance = form.save(commit=False)
            customs_clearance.booking = booking  
            customs_clearance.save()
            messages.success(request, 'Customs clearance (Export) has been processed successfully!')
            return redirect('export_clearance_detail', clearance_id=customs_clearance.id)
    else:
        form = CustomsClearanceExportForm()
    return render(request, 'couriers/create_export_clearance.html', {'form': form, 'booking': booking})

def create_import_clearance(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = CustomsClearanceImportForm(request.POST)
        if form.is_valid():
            customs_clearance = form.save(commit=False)
            customs_clearance.booking = booking 
            customs_clearance.save()
            messages.success(request, 'Customs clearance (Import) has been processed successfully!')
            return redirect('import_clearance_detail', clearance_id=customs_clearance.id)
    else:
        form = CustomsClearanceImportForm()
    return render(request, 'couriers/create_import_clearance.html', {'form': form, 'booking': booking})

def export_clearance_detail(request, clearance_id):
    clearance = CustomsClearanceExport.objects.get(id=clearance_id)
    return render(request, 'couriers/export_clearance_detail.html', {'clearance': clearance})

def import_clearance_detail(request, clearance_id):
    clearance = CustomsClearanceImport.objects.get(id=clearance_id)
    return render(request, 'couriers/import_clearance_detail.html', {'clearance': clearance})





def create_last_mile_delivery(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = LastMileDeliveryForm(request.POST)
        if form.is_valid():
            last_mile_delivery = form.save(commit=False)
            last_mile_delivery.booking = booking
            last_mile_delivery.save()
            return redirect('last_mile_delivery_detail', delivery_id=last_mile_delivery.id)
    else:
        form = LastMileDeliveryForm()
    return render(request, 'couriers/create_last_mile_delivery.html', {'form': form, 'booking': booking})

def last_mile_delivery_detail(request, delivery_id):
    delivery = LastMileDelivery.objects.get(id=delivery_id)
    return render(request, 'couriers/last_mile_delivery_detail.html', {'delivery': delivery})

def update_delivery_status(request, delivery_id):
    delivery = LastMileDelivery.objects.get(id=delivery_id)
    if request.method == 'POST':
        form = LastMileDeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('last_mile_delivery_detail', delivery_id=delivery.id)
    else:
        form = LastMileDeliveryForm(instance=delivery)
    return render(request, 'couriers/update_delivery_status.html', {'form': form, 'delivery': delivery})




def home_view(request):
    return render(request, 'couriers/home.html')

def about_view(request):
    return render(request, 'couriers/about.html')

def contact_view(request):
    return render(request, 'couriers/contact.html')