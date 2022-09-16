from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product/create', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('auth/', include(router.urls)),
    path('auth/login/', signIn, name='login'),
    path('auth/logout/<int:pk>/', signOut, name='logout'),
]