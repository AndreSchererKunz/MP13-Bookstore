from django.test import TestCase
from product.serializers import CategorySerializer
from product.factories import CategoryFactory


class CategorySerializerTest(TestCase):
    def test_category_serializer_data(self):
        category = CategoryFactory()
        serializer = CategorySerializer(instance=category)
        data = serializer.data

        self.assertEqual(data["title"], category.title)
        self.assertEqual(data["slug"], category.slug)
        self.assertEqual(data["description"], category.description)
        self.assertEqual(data["active"], category.active)
