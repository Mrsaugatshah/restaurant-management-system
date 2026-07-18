from django.contrib import admin
from .models import Table,MenuItem,Category,Order,OrderItem,KitchenStation
from .models import OrderHistory
# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display=["name","is_reserved"]
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=["name","default_priority"]
    
    
admin.site.register(Category)
admin.site.register(KitchenStation)
admin.site.register(OrderHistory)
admin.site.register(OrderItem)

@admin.register(Order)
class OrderAmin (admin.ModelAdmin):
    list_display=["table","status","created_at"]