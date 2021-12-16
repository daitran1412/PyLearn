from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def welcome(request):
    return render(request, 'main/welcome.html')

def login(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'main/login.html', context)

def register(request):
    return render(request, 'main/register.html')