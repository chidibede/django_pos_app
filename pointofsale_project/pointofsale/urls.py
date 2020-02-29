from django.urls import path
from pointofsale import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='pointofsale-home'),
    path('dashboard/', views.dashboard, name='pointofsale-dashboard'),
    path('inventory/', views.inventory, name='pointofsale-inventory'),
    path('sales/', views.SalesView.as_view(), name='pointofsale-sales'),
    path('report/', views.report, name='pointofsale-report'),
    path('order_summary/', views.OrderSummaryView.as_view(), name='order-summary'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='pointofsale-product-details'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart-quantity/<int:pk>/', views.add_to_cart_quantity, name='add-to-cart-quantity'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove_single_item_from_cart/<int:pk>/', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('stock_product/', views.stock_product, name='stock_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('receive_payment/', views.receive_payment, name='receive_payment'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)