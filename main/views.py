from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from .models import User, Category, Store, Product
from .serializers import UserSerializer, CategorySerializer, StoreSerializer, ProductSerializer, SignupSerializer, SigninSerializer
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]  # Require authentication for User API

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Require authentication for Category API

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    #permission_classes = [IsAuthenticated]  # Require authentication for Store API

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticated]  # Require authentication for Product API

class SignupAPIView(APIView):
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to hit this endpoint

    @swagger_auto_schema(request_body=SignupSerializer, responses={201: 'Token'})
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=201)
        return Response(serializer.errors, status=400)
    
class SigninAPIView(APIView):
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to hit this endpoint

    @swagger_auto_schema(
        request_body=SigninSerializer,
        responses={200: 'Token', 401: 'Invalid credentials'}
    )
    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        password =  request.data.get('password')

        # Check if a user with the given username exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=401)

        # Authenticate the user with the provided password
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token associated with the user
        Token.objects.filter(user=request.user).delete()
        return Response({'detail': 'Successfully logged out.'})



