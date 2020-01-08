from django.urls import path
from pointofsale import views

urlpatterns = [
    path('', views.home, name='pointofsale-home'),
    path('dashboard/', views.dashboard, name='pointofsale-dashboard'),
    path('inventory/', views.inventory, name='pointofsale-inventory'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('stock_product/', views.stock_product, name='stock_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    
]
