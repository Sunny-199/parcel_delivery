# Generated by Django 3.1.12 on 2022-05-18 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_contact_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contacts',
        ),
    ]
