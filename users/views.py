from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

def login_view(request):
    if request.method == 'POST': 
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')  
            else:
                return redirect('user_dashboard')  
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect('account/login.html') 
        
    return render(request, 'account/login.html')  




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        role = request.POST.get('role')  

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'account/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'account/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
            return render(request, 'account/register.html')


        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


        if role == "Admin":
            admin_group,created = Group.objects.get_or_create(name="Admin")
            user.groups.add(admin_group)
        else:
            user_group, created = Group.objects.get_or_create(name="User")
            user.groups.add(user_group)

        messages.success(request, "Your account has been created successfully!")
        return redirect('login')

    return render(request, 'account/register.html')


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')


