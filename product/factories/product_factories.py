import factory
from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    description = factory.Faker("sentence")
    price = factory.Faker("pyint", min_value=10, max_value=1000)
    active = True

    class Meta:
        model = Product

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if create and extracted:
            self.category.set(extracted)
