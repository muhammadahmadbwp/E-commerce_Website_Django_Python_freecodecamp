# Generated by Django 4.1.7 on 2023-04-13 12:28

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_order_billing_address"),
    ]

    operations = [
        migrations.RemoveField(model_name="billingaddress", name="countries",),
        migrations.AddField(
            model_name="billingaddress",
            name="country",
            field=django_countries.fields.CountryField(default="China", max_length=2),
            preserve_default=False,
        ),
    ]
