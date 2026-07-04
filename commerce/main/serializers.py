
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class ReviewSerializer(serializers.ModelSerializer):
    def validate_rating(self,value):
        if value <=0 or value >=11:
            raise serializers.ValidationError('natori malumot kirgizilgan')
        return value

    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer (serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    def validate_price(self,value):
        if value <= 0 :
            raise serializers.ValidationError('price 0 dan baland bolishi kerak')
        return value

    def validate_stock(self,value):
        if value < 0:
            raise serializers.ValidationError('manfiy bolishi mumkin emas')
        return value


    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    def validate_name(self,value):
        if not value.strip():
            raise serializers.ValidationError('category nomi bosh bolishui mumkin emas!')
        return value
    class Meta:
        model = Category
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    def validate_quantity(self,value):
        if value <=0:
            raise serializers.ValidationError('0 yoki minus bolmasligi kerak')
        return value

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    def validate_quantity(self,value):
        if value <= 0:
            raise serializers.ValidationError('0 dan baland bolishi kerak')
        return value

    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('narx faqat musbat bolishi kerak')
        return value

    def validate(self,attrs):
        if attrs['product'].stock < attrs['quantity']:
            raise serializers.ValidationError('Soralgan miqdorda mahsulot yetarli emas')
        return attrs

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

