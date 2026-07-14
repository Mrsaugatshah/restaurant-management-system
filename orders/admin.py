from django.contrib import admin
from .models import Table,MenuItem,Category,Order,OrderItem
from .models import OrderHistory
# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display=["name","is_reserved"]
    
    
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(OrderHistory)
admin.site.register(OrderItem)

@admin.register(Order)
class OrderAmin (admin.ModelAdmin):
    list_display=["table","status","created_at"]