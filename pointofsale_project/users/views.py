from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def employee(request):
    context = {
        'employees': User.objects.all()
    }
    return render(request, 'users/employee.html', context)

@login_required
def profile(request):
    current_time = timezone.localtime(timezone.now())
    context ={
        "current_time": current_time
    }
    return render(request, 'users/profile.html', context)

def update_employee(request):
    if request.method =='POST':
        employee_id = request.POST['employee_id']
        employee_firstname = request.POST['firstname']
        employee_lastname = request.POST['lastname']
        employee_username = request.POST['username']
        employee_email = request.POST['email']
        User.objects.filter(pk=int(employee_id)).update(id=int(employee_id), first_name=employee_firstname, 
                                    last_name=employee_lastname, username= employee_username, email=employee_email)
        
        messages.success(request, f'Staff Updated Successfully')
        return redirect('users-employee')

def delete_employee(request):
    if request.method =='POST':
        employee_id = request.POST['employee_id']
        User.objects.filter(pk=int(employee_id)).delete()
        
        messages.success(request, f'Staff Deleted Successfully')
        return redirect('users-employee')