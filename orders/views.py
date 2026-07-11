from django.shortcuts import render
from .decorators import role_required
from accounts.models import User
from .models import Table,Category


@role_required([User.Role.WAITER])
def tables_views(request):
   
    tables=Table.objects.all()
    return render(request, "orders/tables.html", {"tables": tables})



@role_required([User.Role.WAITER])
def menu_views(request,table_id):
   
     categories=Category.objects.all()
     return render(request, "orders/menu.html", {"categories": categories,'table_id':table_id})

