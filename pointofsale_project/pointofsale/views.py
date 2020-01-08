from django.shortcuts import render, redirect
from django.contrib import messages
from pointofsale.forms import AddCategoryForm, AddProductForm, UpdateProductForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from pointofsale.models import Product

# Create your views here.
def home(request):
    return render(request, 'pointofsale/home.html')

def dashboard(request):
    return render(request, 'pointofsale/dashboard.html')

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
        category = update_form.data['category']
        product = Product.objects.filter(pk=int(product_id)).update(id=int(product_id), name=name, description=desc, cost_price=cost_price,
                                            selling_price=selling_price, category_id=int(category))
        
        messages.success(request, f'Product Updated Successfully')
        return redirect('pointofsale-inventory')
    
def stock_product(request):
    if request.method =='POST':
        product_id = request.POST['product_id']
        quantity_kg = request.POST['quantity_kg']
        quantity_units = request.POST['quantity_units']
        product = Product.objects.filter(pk=int(product_id)).update(quantity_kg=quantity_kg, quantity_units=quantity_units)
        
        messages.success(request, f'Product Stocked Successfully')
        return redirect('pointofsale-inventory')

def delete_product(request):
    if request.method =='POST':
        product_id = request.POST['product_id']
        product = Product.objects.filter(pk=int(product_id)).delete()
        
        messages.success(request, f'Product Deleted Successfully')
        return redirect('pointofsale-inventory')