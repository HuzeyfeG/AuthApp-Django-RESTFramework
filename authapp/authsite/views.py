from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
import requests

# Create your views here.


@api_view(["GET"])
def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {"message": "Welcome " + request.user.username})
    else:
        return render(request, "index.html", {"message": "Welcome Stranger! Login or Signup"})

@api_view(["GET", "POST"])
def loginReq(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]
        res = requests.post("http://localhost:8000/api-auth/login", data={"username": username, "password": password})
        if res.status_code == 200:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        else:
            return render(request, "login.html", {"message": res.json()["message"]})
    else:
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return render(request, "login.html")

@api_view(["GET", "POST"])
def signupReq(request):
    if request.method == "POST":
        username = request.data["username"]
        email = request.data["email"]
        password = request.data["password"]
        res = requests.post("http://localhost:8000/api-auth/signup", data={"username": username, "email": email, "password": password})
        if res.status_code == 200:
            return render(request, "signup.html", {"message": res.json()["message"]})
        else:
            return render(request, "signup.html", {"message": res.json()["message"]})
    else:
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return render(request, "signup.html")


def logoutReq(request):
    logout(request)
    return redirect("login")
