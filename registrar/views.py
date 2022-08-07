from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            newUser = User.objects.create(
                username = form.cleaned_data["username"],
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                email = form.cleaned_data["email"],
            )
            newUser.set_password(form.cleaned_data["password1"])
            newUser.save()

    return render(request, 'register.html', {'form': form})

def signin(request):
    
    user_form = LoginForm()
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        
        if user_form.is_valid():            
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'signin.html', {'form':user_form})


def signout(request):
    logout(request)
    return redirect('/')