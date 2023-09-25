from django.urls import path
from .views import dashboard, create_shipment, shipments



urlpatterns = [
    path('create-shipment/', create_shipment, name="create-shipment" ),
    path('shipments/', shipments, name="shipments" ),
    path('<str:username>/', dashboard, name="client-dashboard" ),
]