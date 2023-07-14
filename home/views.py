from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from home.models import CustomUser as User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password


@login_required
def home(request):
    context = {
        'isLogin': request.user.username
    }
    return render(request, 'home.html', context)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()
        if user and check_password(password, user.password):
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {"error": "Username or password is wrong!"})

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        hash_pass = make_password(password)

        try:
            User.objects.create(username=username, mobile=mobile, name=name, password=hash_pass, email=email)
        except IntegrityError:
            return render(request, 'signup.html', {'msg': 'Username or Mobile already exist!'})

        return redirect('login')

    return render(request, 'signup.html')


def custom_logout(request):
    logout(request)
    return redirect('login')
