# Generated by Django 3.0.2 on 2020-03-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsale', '0012_remove_purchase_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='month',
            field=models.IntegerField(default=3),
        ),
    ]
