from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponse

from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('Registration success')
    else:
        user_form = RegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})

#login
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('Login failed')
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
           
    