from django.contrib.auth import authenticate, login, logout
from dashboard.models import BusAndRoutes, BusRegistartion, CompanyStaff
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from dashboard.forms import registerUser

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('home_dashboard'))
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'authentication/login.html')

def get_registration(request):
    form = registerUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, 'Registartion done successfuly')
        return redirect('/authentication/user/auth/login/')
    context = {
        'form':form,
    }
    return render(request, 'authentication/user_registration.html', context)

def register(request):
    return render(request, 'authentication/register.html')

def company_login(request):
    return render(request, 'authentication/company_login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_user_authentication'))
