from django.shortcuts import render
from .decorators import role_required
from accounts.models import User
from .models import Table


@role_required([User.Role.WAITER])
def tables_views(request):
    tables = Table.objects.all()
    return render(request, "orders/tables.html", {"tables": tables})