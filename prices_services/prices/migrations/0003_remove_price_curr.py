# Generated by Django 5.1.1 on 2024-09-12 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("prices", "0002_alter_price_brand_id_alter_price_curr_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="curr",
        ),
    ]
