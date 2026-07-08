from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            print("login successful")
            messages.success(request, "login successful")
            return redirect("tables_view_url")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login_view_url")
        
    return render(request, "accounts/login.html")