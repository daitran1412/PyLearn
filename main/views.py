from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.

def welcome(request):
    return render(request, 'main/welcome.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tạo tài khoản thành công!')
                return redirect('login')
        context = {'form': form}
        return render(request, 'main/register.html', context)
    
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                messages.success(request, ('Đăng nhập thành công!'))
                return redirect('home')
            else:
                messages.success(request, ('Tên tài khoản hoặc mật khẩu không đúng! Xin hãy thử lại!'))
                return redirect('login')
        return render(request, 'main/login.html')

def logout(request):
    django_logout(request)
    return redirect('welcome')

@login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html')