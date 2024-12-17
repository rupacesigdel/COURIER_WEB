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
    path('booking/<int:booking_id>/create_export_clearance/', views.create_export_clearance, name='create_export_clearance'),
    path('booking/<int:booking_id>/create_import_clearance/', views.create_import_clearance, name='create_import_clearance'),
    path('pickup/create/<int:booking_id>/', views.create_pickup, name='create_pickup'),
    path('pickup/<int:pickup_id>/', views.pickup_detail, name='pickup_detail'),
    path('export_clearance/<int:clearance_id>/', views.export_clearance_detail, name='export_clearance_detail'),
    path('import_clearance/<int:clearance_id>/', views.import_clearance_detail, name='import_clearance_detail'),
    path('booking/<int:booking_id>/create_last_mile_delivery/', views.create_last_mile_delivery, name='create_last_mile_delivery'),
    path('last_mile_delivery/<int:delivery_id>/', views.last_mile_delivery_detail, name='last_mile_delivery_detail'),
    path('last_mile_delivery/<int:delivery_id>/update/', views.update_delivery_status, name='update_delivery_status'),
    path('sorting_hub/', views.sorting_hub, name='sorting_hub'),
    path('sort_items/', views.sort_items, name='sort_items'),
]
