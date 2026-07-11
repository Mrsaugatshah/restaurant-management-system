from django.contrib import admin
from .models import Table,MenuItem,Category

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display=["name","is_reserved"]
    
    
admin.site.register(Category)
admin.site.register(MenuItem)