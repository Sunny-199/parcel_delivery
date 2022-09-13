from wsgiref.util import shift_path_info
from rest_framework import serializers
from .models import ShipmentsPurpleShip, Payment, Shipper, Recipient, Options


class ShipmentsPurpleShipSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShipmentsPurpleShip
        fields = '__all__'


class ShipperSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'


class Recipt2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class OptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class RecipientSerializers(serializers.Serializer):
    country_code = serializers.CharField()
    postal_code = serializers.CharField()
    city = serializers.CharField()
    federal_tax_id = serializers.CharField()
    state_tax_id = serializers.CharField()
    person_name = serializers.CharField()
    company_name = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.IntegerField()
    state_code = serializers.IntegerField()
    suburb = serializers.CharField()
    residential = serializers.CharField()
    address_line1 = serializers.CharField()
    address_line2 = serializers.CharField()
    validate_location = serializers.CharField()


class ParcelsSerializers(serializers.Serializer):
    weight = serializers.CharField()  # The parcel's weight
    weight_unit = serializers.CharField()  # The parcel's weight unit
    width = serializers.CharField()  # The parcel's width
    height = serializers.CharField()  # The parcel's height
    length = serializers.CharField()  # The parcel's length
    packaging_type = serializers.CharField()  # The parcel's packaging type.For specific carriers packaging type, please consult the reference.
    package_preset = serializers.CharField()  # The parcel's package preset.
    description = serializers.CharField()  # The parcel's description
    content = serializers.CharField()  # The parcel's content description
    is_document = serializers.CharField()  # Indicates if the parcel is composed of documents only
    dimension_unit = serializers.CharField()  # The parcel's dimension unit
