# Generated by Django 5.0.7 on 2024-08-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomhub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
