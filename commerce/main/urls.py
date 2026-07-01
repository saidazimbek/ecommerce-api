from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegisterAPIView.as_view()),
    path('categories/',CategoryListCreateAPIAView.as_view()),
    path('categories/<int:pk>/',CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('products/',ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/',ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('reviews/',ReviewListCreateAPIView.as_view()),
    path('reviews/<int:pk>/',ReviewRetrieveUpdateDestroyAPIView.as_view()),
    path('carts/',CartListCreateAPIView.as_view()),
    path('carts/<int:pk>/',CartRetrieveUpdateDestroyAPIView.as_view()),
    path('cartitems/',CartItemListCreateAPIView.as_view()),
    path('cartitems/<int:pk>/',CartItemRetrieveUpdateDestroyAPIView.as_view()),
    path('orders/',OrderListCreateAPIView.as_view()),
    path('orders/<int:pk>/',OrderRetrieveUpdateDestroyAPIView.as_view()),
    path('orderitems/',OrderItemListCreateAPIView.as_view()),
    path('orderitems/<int:pk>/',OrderItemRetrieveUpdateDestroyAPIView.as_view()),
    path('wishlists/',WishlistListCreateAPIView.as_view()),
    path('wishlists/<int:pk>/',WishlistRetrieveUpdateDestroyAPIView.as_view()),
]