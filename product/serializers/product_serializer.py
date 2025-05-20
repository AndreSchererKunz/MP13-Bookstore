from rest_framework import serializers

from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product 
        fields = [
            'id',
            'title',
            'description',
            'price', 
            'active',
            'category',
            'categories_id'
    ]

    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')
        product = Product.objects.create(**validated_data)
        product.category.set(category_data)
        return product