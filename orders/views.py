from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .forms import RegistrationForm


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/user.html", context)

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.cleaned_data)
            return render(request, 'orders/signup.html', {'form': form, 'message': 'Invalid information.'})
    
    elif request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'orders/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials.", 'user': user})

    elif request.method == 'GET':
        return render(request, 'orders/login.html', {'message': None})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def cart_view(request):
    return render(request, 'orders/cart.html')