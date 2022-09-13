from multiprocessing import managers
from multiprocessing.spawn import import_main_path
from operator import imod
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import *


# Create your views here.


class ShipmentsPurpleshipViewset(ModelViewSet):
    queryset = ShipmentsPurpleShip.objects.all()
    serializer_class = ShipmentsPurpleShipSerializers

    def list(self, request, *args, **kwargs):
        queryset = ShipmentsPurpleShip.objects.all()
        serializer = ShipmentsPurpleShipSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShipperViewset(ModelViewSet):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializers


class ReciptViewset(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = Recipt2Serializers


class OptionsViewset(ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializers


class PaymentsViewset(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class RecipientViewset(viewsets.ViewSet):
    serializer_class = RecipientSerializers

    def create(self, request, *args, **kwargs):
        # serializer_class = self.get_serializer_class()
        serializer = RecipientSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        data = {"status": True}
        return Response(data)


class ParcelViewset(viewsets.ViewSet):
    serializer_class = ParcelsSerializers

    def create(self, request, *args, **kwargs):
        # serializer_class = self.get_serializer_class()
        serializer = ParcelsSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # data = {"status": True}
        return Response(serializer.data)
