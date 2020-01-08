from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    # roles =[("Admin", "Admin"), ("financial_manager", "Financial Manager"), ("operator", "Operator")]
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # role = forms.ChoiceField(choices=roles, label="Roles")
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
        }


       