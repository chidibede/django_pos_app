# Generated by Django 3.0.2 on 2020-01-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsale', '0012_auto_20200111_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
