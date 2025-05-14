from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), write_only=True
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum(p.price for p in instance.product.all())
        return total

    def create(self, validated_data):
        product_ids = validated_data.pop('product_ids')
        order = Order.objects.create(**validated_data)
        order.product.set(product_ids)
        return order

    class Meta:
        model = Order
        fields = ['user', 'product', 'product_ids', 'total']