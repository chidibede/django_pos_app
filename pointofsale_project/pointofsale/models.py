from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_kg = models.IntegerField(default=0)
    quantity_units = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    image_field = models.ImageField(default='default.jpg', upload_to='uploaded_images')
    date_created = models.DateTimeField(default=timezone.now)
    staff = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
