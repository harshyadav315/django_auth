
from django.shortcuts import render,HttpResponse,redirect
from requests import request
from .forms import CreateUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.user.is_authenticated :
        print(request.user)

    return render(request,"index.html")

def signup(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account was created for "+str(form.cleaned_data.get("username")))
            # print(request.POST.get("username"))
            return redirect("login")


        # print(request.POST.get("username"))

    return render(request,"signup.html")

def handle_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"Username or Password is Incorrect !!!")
            return render(request,"login.html")

    return render(request,"login.html")


def handle_logout(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def access(request):

    return render(request,"access.html")
