# Generated by Django 3.0.2 on 2020-03-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsale', '0009_auto_20200305_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitem',
            name='month',
            field=models.IntegerField(default=3),
        ),
    ]
