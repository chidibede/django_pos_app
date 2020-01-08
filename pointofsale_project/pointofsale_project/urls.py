
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Asua Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pointofsale.urls')),
    path('', include('users.urls')),
]
