# Generated by Django 4.0.3 on 2022-04-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
