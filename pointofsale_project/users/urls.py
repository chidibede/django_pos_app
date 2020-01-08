from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('register/', user_views.register, name='users-register'),
    path('employee/', user_views.employee, name='users-employee'),
    path('profile/', user_views.profile, name='users-profile'),
    path('update_employee/', user_views.update_employee, name='update_employee'),
    path('delete_employee/', user_views.delete_employee, name='delete_employee'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='users-logout'),
]