# Generated by Django 3.1.7 on 2021-03-30 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='notes',
            field=models.TextField(default=None),
        ),
    ]
