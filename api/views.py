import re
import uuid
import random
from django.db.models import Q
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer


@csrf_exempt
def signIn(request):

    if request.method == 'POST':
        username = request.data.get('email')
        password = request.data.get('password')
        if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
            return JsonResponse({'error': 'Please Enter a valid Email'})
        if len(password) < 5:
            return JsonResponse({'error': 'Password must be atleast 5 characters long'})
        
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email = username)
            if user.check_password(password):
                get_user = UserModel.objects.filter(email = username).values().first()
                get_user.pop('password')
                user.save()
                login(request, user)
            else:
                return JsonResponse({'error': 'Invalid Password'})
        except:
            return JsonResponse({'error': 'Invalid Email!'})
    return JsonResponse({'error': 'Method not allowed'})


def signOut(request, id):
    
    logout(request)
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user'})
    return JsonResponse({'Success': 'Successfylly Logged Out'})


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_class = []
        if self.action == 'create' or self.action == 'reterive':
            permission_class = [AllowAny]
        elif self.action == 'reterive' or self.action == 'update' or self.action == 'partial_update':
            permission_class = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


class ProductListAPIView(ListAPIView):

    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductCreateAPIView(CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDetailAPIView(RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDeleteAPIView(DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]