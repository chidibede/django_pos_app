from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



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
    image_field = models.ImageField(default='default.jpg')
    date_created = models.DateTimeField(default=timezone.now)
    staff = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pointofsale-product-details', kwargs={'pk': self.pk})
    
    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={'pk': self.pk})
    
    def get_remove_from_cart_url(self):
        return reverse('remove-from-cart', kwargs={'pk': self.pk})
    

    

class PurchaseItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)

    
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}" 

    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(PurchaseItem)
    total_price = models.IntegerField(default=0)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
