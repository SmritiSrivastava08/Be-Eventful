# Generated by Django 4.0 on 2022-05-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeEventful', '0021_feedbackdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdetails',
            name='Status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
