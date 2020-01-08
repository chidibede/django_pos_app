# Generated by Django 3.0.2 on 2020-01-07 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pointofsale', '0003_remove_product_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_field',
            field=models.ImageField(default='default.jpg', upload_to='uploaded_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
