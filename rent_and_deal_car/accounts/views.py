from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.models import auth

User = get_user_model()


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(email=email, password=password, first_name=first_name,
                                                last_name=last_name)
                user.save()

                return redirect('login_user')

        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)

    else:
        return render(request, 'registeration/registeration.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')

    else:
        return render(request, 'login/login.html')


def home(request):
    return render(request, 'car_rent/base.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')




