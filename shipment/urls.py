from django.urls import path
from shipment.views import (
    index, contact, track_item,
    about,services, editStatus,
    editSender, editClient, editItem,
)

# app_name = 'shop'

urlpatterns = [
    path('', index, name='shipment_index'),
    path('about/', about, name='shipment_about'),
    path('contact/', contact, name='contact'), 
    path('tracking/', track_item, name='shipment_track'),
    path('service/', services, name='shipment_service'),  
    path('edit/sender/<str:slug>/<int:id>/', editSender, name='edit_sender'), 
    path('edit/client/<str:slug>/<int:id>/', editClient, name='edit_client'), 
    path('edit/item/<str:slug>/<int:id>/', editItem, name='edit_item'), 
    path('edit/status/<int:id>/', editStatus, name='edit_status'),  
]