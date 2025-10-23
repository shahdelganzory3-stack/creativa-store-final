from django.contrib import admin
from .models import Category, Product, Order, OrderItem


admin.site.register(Category)

admin.site.register(Product) 



class OrderItemInline(admin.TabularInline):
    model = OrderItem
   
    raw_id_fields = ['product'] 



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  
    list_display = ['id', 'name', 'phone', 'paid', 'created']
  
    list_filter = ['paid', 'created', 'updated']
  
    inlines = [OrderItemInline] 
