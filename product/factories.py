import factory
from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    description = factory.Faker("sentence")
    price = factory.Faker("pyint", min_value=10, max_value=1000)
    active = True
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if create and extracted:
            self.category.set(extracted)
