# Generated by Django 4.0 on 2022-02-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeEventful', '0019_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]