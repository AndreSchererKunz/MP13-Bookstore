from django.test import TestCase
from product.serializers import ProductSerializer
from product.factories import ProductFactory, CategoryFactory


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.categories = CategoryFactory.create_batch(2)
        self.product = ProductFactory(category=self.categories)

    def test_product_serializer_data(self):
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data

        self.assertEqual(data["title"], self.product.title)
        self.assertEqual(data["description"], self.product.description)
        self.assertEqual(data["price"], self.product.price)
        self.assertEqual(data["active"], self.product.active)
        self.assertEqual(len(data["category"]), 2)
