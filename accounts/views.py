from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from .models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")

            if remember_me:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            else:
                request.session.set_expiry(0)

            if user.role == User.Role.WAITER:
                return redirect("tables_view_url")

            elif user.role == User.Role.KITCHEN:
                return redirect("kitchen_dashboard_view_url")

            return redirect("tables_view_url")

        else:
            messages.error(request, "Invalid credentials")
            return redirect("login_view_url")

    return render(request, "accounts/login.html")