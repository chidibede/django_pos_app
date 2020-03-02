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
    quantity = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    total_cost_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
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
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)
    amount_entered = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}" 
    
    def get_total_item_price(self):
        return self.quantity * self.product.selling_price
    
    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()
    
    
    
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(PurchaseItem)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    total_amount = models.IntegerField(default=0)
    purchased = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for purchase_item in self.product.all():
            total += purchase_item.get_final_price()
        return total

class Accounting(models.Model):
    operational_cost = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add = True)


    