# Generated by Django 4.1.5 on 2023-01-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliveryoptions",
            name="delivery_price",
            field=models.DecimalField(
                decimal_places=2,
                error_messages={
                    "name": {"max_length": "The price must be between 0 and 999.99."}
                },
                help_text="Maximum 999.99",
                max_digits=10,
                verbose_name="delivery price",
            ),
        ),
    ]
