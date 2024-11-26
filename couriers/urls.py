from django.urls import path
from . import views
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('api/orders/', OrderListView.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('booking/create/', views.create_booking, name='create_booking'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('pickup/create/<int:booking_id>/', views.create_pickup, name='create_pickup'),
    path('pickup/<int:pickup_id>/', views.pickup_detail, name='pickup_detail'),
    path('sorting_hub/', views.sorting_hub, name='sorting_hub'),
    path('sort_items/', views.sort_items, name='sort_items'),
]
