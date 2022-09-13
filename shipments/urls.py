from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'ship', ShipmentsPurpleshipViewset, basename='ship')
router.register(r'shipper', ShipperViewset, basename='shipper')
router.register(r'recipient', RecipientViewset, basename='recipient')
router.register(r'parcels', ParcelViewset, basename='parcels')
router.register(r'receipt2', ParcelViewset, basename='receipt2')
router.register(r'options', OptionsViewset, basename='options')
router.register(r'payments', PaymentsViewset, basename='payments')

urlpatterns = [
    path('', include(router.urls))
]
