from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import ProductViewSet, OrderViewSet, UserStatusView 



router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product') 
router.register(r'orders', OrderViewSet, basename='order')     



urlpatterns = [
   
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserStatusView.as_view(), name='user_status'), 
    
    
    path('', include(router.urls)), 
]