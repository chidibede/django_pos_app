# Generated by Django 3.0.2 on 2020-01-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsale', '0016_auto_20200112_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='amount_entered',
            field=models.IntegerField(default=0),
        ),
    ]
