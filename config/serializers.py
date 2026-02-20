from rest_framework import serializers
from cart.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def validate(self, data):
        cart = data['cart']
        book = data['book']
        if CartItem.objects.filter(cart=cart, book=book).exists():
            raise serializers.ValidationError("Already in cart")
        return data
