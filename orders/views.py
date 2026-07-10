from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from accounts.models import User
# Create your views here.
@role_required([User.Role.WAITER])
def tables_views(request):
    return render(request, "orders/tables.html")