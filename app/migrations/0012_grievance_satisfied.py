# Generated by Django 4.2.7 on 2023-11-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_grievance_handler_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievance',
            name='satisfied',
            field=models.BooleanField(default=False),
        ),
    ]
