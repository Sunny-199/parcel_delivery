# Generated by Django 3.2.6 on 2022-07-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0005_alter_shipmentspurpleship_test_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('federal_tax_id', models.CharField(max_length=255)),
                ('state_tax_id', models.CharField(max_length=255)),
                ('person_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.BigIntegerField()),
                ('state_code', models.CharField(max_length=200)),
                ('suburb', models.CharField(max_length=200)),
                ('residential', models.CharField(max_length=255)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('validate_location', models.CharField(max_length=255)),
            ],
        ),
    ]
