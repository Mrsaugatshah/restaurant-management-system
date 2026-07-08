from django.shortcuts import render

# Create your views here.
def tables_views(request):
    return render(request, "orders/tables.html")