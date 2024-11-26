from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render, redirect
from rest_framework.exceptions import PermissionDenied
from .models import Booking, Pickup
from .forms import BookingForm, PickupForm
from django.http import HttpResponse
from .forms import SortingForm  
from django.contrib import messages

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
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
            pickup = form.save(commit=False)
            pickup.booking = booking  # Link pickup to the booking
            pickup.save()
            return redirect('pickup_detail', pickup_id=pickup.id)  # Redirect to pickup detail
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

def home_view(request):

    return render(request, 'couriers/home.html')


def about_view(request):

    return render(request, 'couriers/about.html')


def contact_view(request):

    return render(request, 'couriers/contact.html')
