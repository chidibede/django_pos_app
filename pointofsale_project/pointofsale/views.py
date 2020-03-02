import json
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from pointofsale.forms import AddCategoryForm, AddProductForm, UpdateProductForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DetailView, View
from pointofsale.models import Product, Purchase, PurchaseItem
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import FileResponse
from django.db.models import Sum










# Create your views here.
def home(request):
    return render(request, 'pointofsale/home.html')

def dashboard(request):
    products = Product.objects.all()
    total_sales = Purchase.objects.aggregate(Sum('total_amount'))['total_amount__sum']
    purchase_number = Purchase.objects.all().count()
    category_form = AddCategoryForm()
    product_form = AddProductForm()
    update_form = UpdateProductForm()
    context = {
        'category_form': category_form, 
        'product_form': product_form,
        'update_form': update_form,
        'products': products,
        'purchase_number': purchase_number,
        'total_sales': total_sales,
        }
    return render(request, 'pointofsale/dashboard.html', context)



def inventory(request):
    products = Product.objects.all()
    category_form = AddCategoryForm()
    product_form = AddProductForm()
    update_form = UpdateProductForm()
    context = {
        'category_form': category_form, 
        'product_form': product_form,
        'update_form': update_form,
        'products': products,
        }
    return render(request, 'pointofsale/inventory.html', context)

def report(request):
    purchases = PurchaseItem.objects.all()
    total_sales = Purchase.objects.aggregate(Sum('total_amount'))['total_amount__sum']
    context = {
        'purchases': purchases,
        'total_sales': total_sales,
    }
    return render(request, 'pointofsale/report.html', context)

def add_category(request):
    if request.method == 'POST':
        category_form = AddCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            name = category_form.cleaned_data.get('name')
            messages.success(request, f'{name} Category Added Successfully')
            return redirect('pointofsale-inventory')
    else:
        category_form = AddCategoryForm()
    return render(request, 'pointofsale/inventory.html', {'category_form': category_form})

def add_product(request):
    if request.method == 'POST':
        product_form = AddProductForm(request.POST)
        if product_form.is_valid():
            Product = product_form.save(commit=False)
            Product.staff = request.user
            image = request.FILES['image_field']
            file_save = FileSystemStorage()
            file_save.save(image.name, image)
            Product.image_field = image
            Product = Product.save()
            name = product_form.cleaned_data.get('name')
            messages.success(request, f'{name} Product Added Successfully')
            return redirect('pointofsale-inventory')
    else:
        product_form = AddProductForm()
    return render(request, 'pointofsale/inventory.html', {'product_form': product_form})

def update_product(request):
    update_form = UpdateProductForm(request.POST)
    if request.method =='POST':
        product_id = request.POST['product_id']
        name = request.POST['name']
        desc = request.POST['desc']
        cost_price = request.POST['cost_price']
        selling_price = request.POST['selling_price']
        discount_price = request.POST['discount_price']
        category = update_form.data['category']
        Product.objects.filter(pk=int(product_id)).update(id=int(product_id), name=name, description=desc, cost_price=cost_price,
                                            selling_price=selling_price,discount_price=discount_price, category_id=int(category))
        
        messages.success(request, f'Product Updated Successfully')
        return redirect('pointofsale-inventory')
    
def stock_product(request):
    if request.method =='POST':
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        Product.objects.filter(pk=int(product_id)).update(quantity=quantity)
        
        messages.success(request, f'Product Stocked Successfully')
        return redirect('pointofsale-inventory')

def delete_product(request):
    if request.method =='POST':
        product_id = request.POST['product_id']
        Product.objects.filter(pk=int(product_id)).delete()
        
        messages.success(request, f'Product Deleted Successfully')
        return redirect('pointofsale-inventory')


class SalesView(ListView):
    model = Product
    template_name = "pointofsale/sales.html"
    context_object_name = "products"
    paginate_by = 8
    ordering = ['-date_created']
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "pointofsale/product-page.html"

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    purchase_item, created = PurchaseItem.objects.get_or_create(product=product, user=request.user, purchased=False)
    purchase_qs = Purchase.objects.filter(user=request.user, purchased=False)
    if purchase_qs.exists():
        purchase = purchase_qs[0]
        if purchase.product.filter(product__id=product.id).exists():
            purchase_item.quantity +=1
            purchase_item.save()
            messages.info(request, "This product quantity has been updated in the receipt")
        else:
            purchase.product.add(purchase_item)
            messages.info(request, "This product has been added to the receipt")

    else:
        ordered_date = timezone.now()
        purchase = Purchase.objects.create(user=request.user, ordered_date=ordered_date)
        purchase.product.add(purchase_item)
    return redirect("pointofsale-sales")

@login_required
def add_to_cart_quantity(request, pk):
    product = get_object_or_404(Product, pk=pk)
    purchase_item, created = PurchaseItem.objects.get_or_create(product=product, user=request.user, purchased=False)
    purchase_qs = Purchase.objects.filter(user=request.user, purchased=False)
    if purchase_qs.exists():
        purchase = purchase_qs[0]
        if purchase.product.filter(product__id=product.id).exists():
            purchase_item.quantity +=1
            purchase_item.save()
            messages.info(request, "This product quantity has been updated in the receipt")
        else:
            purchase.product.add(purchase_item)
            messages.info(request, "This product has been added to the receipt")

    else:
        ordered_date = timezone.now()
        purchase = Purchase.objects.create(user=request.user, ordered_date=ordered_date)
        purchase.product.add(purchase_item)
    return redirect("order-summary")

def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    purchase_qs = Purchase.objects.filter(user=request.user, purchased=False)
    if purchase_qs.exists():
        purchase = purchase_qs[0]
        # check if the order item is in the order
        if purchase.product.filter(product__id=product.id).exists():
            purchase_item = PurchaseItem.objects.filter(product=product, user=request.user, purchased=False)[0]
            purchase.product.remove(purchase_item)
            purchase_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("order-summary")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("order-summary")


def remove_single_item_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    purchase_qs = Purchase.objects.filter(user=request.user, purchased=False)
    if purchase_qs.exists():
        purchase = purchase_qs[0]
        # check if the order item is in the order
        if purchase.product.filter(product__id=product.id).exists():
            purchase_item = PurchaseItem.objects.filter(product=product, user=request.user, purchased=False)[0]
            if purchase_item.quantity > 1:
                purchase_item.quantity -= 1
                purchase_item.save()
            else:
                purchase.product.remove(purchase_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("order-summary")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("order-summary")

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            purchase = Purchase.objects.get(user=self.request.user, purchased=False)
            context = {
                'object': purchase
            }
            return render(self.request, 'pointofsale/receipt.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have any order")
            return redirect('pointofsale-sales')
        


def receive_payment(request):
    if request.method == 'POST':
        purchase = Purchase.objects.get(user=request.user, purchased=False)
        purchase_item = purchase.product.all()
        purchase_item.update(purchased=True)
        for item in purchase_item:
            print(item.product.id)
            print(item.product.quantity)
            print(item.quantity)
            Product.objects.filter(pk=int(item.product.id)).update(quantity=(item.product.quantity - item.quantity))
            item.save()
        purchase.total_amount = purchase.get_total()  
        purchase.purchased = True
        purchase.save()
        messages.success(request, "Payment received successfully")
        return redirect('pointofsale-sales')


