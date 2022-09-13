from pyexpat import model
from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import FieldDoesNotExist
from django.db.models.deletion import RESTRICT

# Choices for Carrier Name have been passed here

CARRIER_NAME = (
    ('aramex', 'Aramex'),
    ('australiapost', 'Australiapost'),
    ('canadapost', 'Canadapost'),
    ('canpar', 'Canpar'),
    ('dhl_express', 'Dhl_Express'),
    ('dhl_universal', 'Dhl_Universal'),
    ('dicom', 'Dicom'),
    ('eshipper', 'Eshipper'),
    ('fedex', 'Fedex'),
    ('freightcom', 'Freightcom'),
    ('purolator', 'Purolator'),
    ('royalmail', 'Royalmail'),
    ('sendle', 'Sendle'),
    ('sf_express', 'Sf_Express'),
    ('tnt', 'Tnt'),
    ('ups', 'Ups'),
    ('usps', 'Usps'),
    ('usps_international', 'Usps_International'),
    ('yanwen', 'Yanwen'),
)
# Choices for status have been passed here
STATUS_CHOICES = (
    ('created', 'Created'),
    ('purchased', 'Purchased'),
    ('cancelled', 'Cancelled'),
    ('shipped', 'Shipped'),
    ('in-transit', 'In-Transit'),
    ('delivered', 'Delivered'),
)
PAID_BY = (
    ('sender', 'Sender'),
    ('recipient', 'Recipient'),
    ('third_party', 'Third_Party'),
)


# COUNTRY_CODE  = (
#     ('AD','AD')
#     ('AE','AE')
# )
# shipments model
class Shipments(models.Model):
    shipment_id = models.CharField(unique=True, max_length=100)
    shipment_reference = models.CharField(unique=True, max_length=100)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


# shipments model for label as per purpleship API provide to us
class ShipmentsPurpleShip(models.Model):
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    test_mode = models.BooleanField()
    created_start = models.DateTimeField(auto_now_add=True)
    created_end = models.DateTimeField(auto_now=True)
    carrier_id = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    limit = models.IntegerField()  # Number of results to return per page.
    offset = models.IntegerField()  # The initial index from which to return the results.
    carrier_name = models.CharField(max_length=255, choices=CARRIER_NAME)


# shipments model for Create a shipment as per purpleship API provide to us 
class Shipper(models.Model):
    country_code = models.CharField(max_length=10, null=True, blank=True)  # Code of a specific country
    postal_code = models.CharField(max_length=20, null=True, blank=True)  # The address postal code
    city = models.CharField(max_length=255, null=True, blank=True)  # The address city.
    federal_tax_id = models.CharField(max_length=255, null=True, blank=True)  # The party federal tax id
    state_tax_id = models.CharField(max_length=255, null=True, blank=True)  # The party state id
    person_name = models.CharField(max_length=255, null=True, blank=True)  # Name of the Shipper
    company_name = models.CharField(max_length=255, null=True, blank=True)  # The company name if the party is a company
    email = models.EmailField(max_length=255, null=True, blank=True)  # Shipper Email
    phone_number = models.BigIntegerField(null=True, blank=True)  # Shippers Phone Number
    state_code = models.CharField(max_length=200, null=True, blank=True)
    suburb = models.CharField(max_length=200, null=True, blank=True)
    residential = models.CharField(max_length=255, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    validate_location = models.CharField(max_length=255, null=True, blank=True)


class Recipient(models.Model):
    country_code = models.CharField(max_length=10)  # Code of a specific country
    postal_code = models.CharField(max_length=20)  # The address postal code
    city = models.CharField(max_length=255)  # The address city.
    federal_tax_id = models.CharField(max_length=255)  # The party federal tax id
    state_tax_id = models.CharField(max_length=255)  # The party state id
    person_name = models.CharField(max_length=255)  # Name of the Shipper
    company_name = models.CharField(max_length=255)  # The company name if the party is a company
    email = models.EmailField()  # Shipper Email
    phone_number = models.BigIntegerField()  # Shippers Phone Number
    state_code = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    residential = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    validate_location = models.CharField(max_length=255)


class Parcel(models.Model):
    weight = models.CharField(max_length=255)
    weight_unit = models.CharField(max_length=255)
    width = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    packaging_type = models.CharField(max_length=255)
    package_preset = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    is_document = models.CharField(max_length=255)
    dimension_unit = models.CharField(max_length=255)


class Options(models.Model):
    property_name = models.CharField(max_length=255)


class Payment(models.Model):
    paid_by = models.CharField(max_length=255, choices=PAID_BY)
    currency = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
