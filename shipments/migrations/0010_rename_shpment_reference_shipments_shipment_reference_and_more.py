# Generated by Django 4.0.6 on 2022-07-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0009_parcel_rename_content_recipient_address_line1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipments',
            old_name='shpment_reference',
            new_name='shipment_reference',
        ),
        migrations.AlterField(
            model_name='shipper',
            name='address_line1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='address_line2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='country_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='federal_tax_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='person_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='residential',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='state_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='state_tax_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='suburb',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='validate_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]