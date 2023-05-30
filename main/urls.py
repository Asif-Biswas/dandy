from django.urls import path
from .views import UserViewSet, CategoryViewSet, StoreViewSet, ProductViewSet


urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('stores/', StoreViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('stores/<int:pk>/', StoreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]