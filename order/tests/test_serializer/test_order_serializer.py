from django.test import TestCase
from order.serializers import OrderSerializer
from product.factories import ProductFactory, CategoryFactory
from order.factories import OrderFactory, UserFactory


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.products = ProductFactory.create_batch(2, category=[self.category])
        self.user = UserFactory()
        self.order = OrderFactory(user=self.user, product=self.products)

    def test_order_total(self):
        serializer = OrderSerializer(instance=self.order)
        data = serializer.data
        expected_total = sum(p.price for p in self.products)

        self.assertEqual(data["total"], expected_total)
        self.assertEqual(len(data["product"]), 2)

    def test_order_creation_with_product_ids(self):
        product_ids = [p.id for p in self.products]
        data = {"user": self.user.id, "product_ids": product_ids}
        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        order = serializer.save()
        self.assertEqual(order.product.count(), 2)
