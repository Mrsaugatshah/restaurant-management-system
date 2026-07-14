from django.shortcuts import render,redirect
from .decorators import role_required
from accounts.models import User
from .models import Table,Category,Order,OrderItem,MenuItem
import json
from django.contrib import messages


@role_required([User.Role.WAITER])
def tables_views(request):
   
    tables=Table.objects.all()
    return render(request, "orders/tables.html", {"tables": tables})



@role_required([User.Role.WAITER])
def menu_views(request, table_id):

    if request.method == "POST":

        data = request.POST.get("order_data")
        data_list = json.loads(data)

        # Get table from URL parameter
        table_obj = Table.objects.get(pk=table_id)

        # Create order
        order = Order.objects.create(
            table=table_obj
        )

        # Create order items
        for orderitem in data_list:

            menu_item = MenuItem.objects.get(
                pk=orderitem.get("id")
            )

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                price=menu_item.price,
                quantity=orderitem.get("qty")
            )

        messages.success(
            request,
            "Order created successfully"
        )

        return redirect("tables_view_url")


    categories = Category.objects.all()
    orders = Order.objects.filter(table_id=table_id
                                  ).exclude(status=Order.ORDER_STATUS.BILLED
                                            ).order_by("-created_at")
    # print(orders)
    # print(orders.count())
    

    return render(
        request,
        "orders/menu.html",
        {
            "categories": categories,
            "table_id": table_id,
            "orders":orders
        }
    )
    print("table_id from URL:", table_id)
