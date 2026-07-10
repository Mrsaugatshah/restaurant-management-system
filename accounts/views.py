from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember")
        
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "login successful")
            # If checkbox is checked `remember_me` will be a non-empty value (e.g. 'on').
            # When checked, set expiry to the configured `SESSION_COOKIE_AGE`.
            # When not checked, expire the session at browser close.
            if remember_me:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            else:
                request.session.set_expiry(0)
            return redirect("tables_view_url")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login_view_url")
        
    return render(request, "accounts/login.html")