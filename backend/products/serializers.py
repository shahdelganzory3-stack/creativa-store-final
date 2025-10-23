from rest_framework import serializers
from .models import Category, Product, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ProductSerializer(serializers.ModelSerializer):
   
    category = CategorySerializer(read_only=True) 
    
    class Meta:
        model = Product
       
        fields = (
            'id', 'category', 'name', 'slug', 'description', 'price', 
            'image', 'available', 'created',
            'available_sizes',    
            'available_colors',   
        )
       


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'price', 'quantity', 'size', 'color')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'address', 'paid', 'created', 'get_total_cost', 'items')
