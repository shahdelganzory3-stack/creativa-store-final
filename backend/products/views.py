from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated 

from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer



class ProductViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

   
    def get_permissions(self):
        """
        يحدد الأذونات بناءً على نوع العملية المطلوبة (GET/POST/PUT/DELETE)
        """
        if self.action in ['list', 'retrieve']:
          
            permission_classes = [permissions.AllowAny] 
        else:
         
            permission_classes = [permissions.IsAdminUser] 

        return [permission() for permission in permission_classes]

# 2. إعدادات OrderViewSet (الطلبات)
class OrderViewSet(viewsets.ModelViewSet):
    
    # 1. تحديد الـ Queryset والـ Serializer
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer

    # 2. تعديل الصلاحيات (Permissions)
    def get_permissions(self):
        """
        يحدد الصلاحيات: إنشاء طلب (POST) متاح للجميع، الباقي للمسجلين.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
            
        return [permission() for permission in permission_classes]
    
    # 3. إضافة دالة perform_create لحفظ المستخدم (إذا كان مسجلاً)
    def perform_create(self, serializer):
        """
        يتم استدعاء هذه الدالة عند إنشاء الطلب.
        إذا كان المستخدم مسجلاً، نقوم بربط الطلب بحسابه.
        """
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
            

    def get_queryset(self):
        user = self.request.user
        
        if user.is_authenticated and (user.is_staff or user.is_superuser):
            return Order.objects.all()
        
        elif user.is_authenticated:
            return Order.objects.filter(user=user)
        
        return Order.objects.none()


class UserStatusView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        user = request.user
     
        return Response({
            'id': user.id,
            'username': user.username,
            'is_staff': user.is_staff,
        })