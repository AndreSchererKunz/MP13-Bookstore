import factory
from django.contrib.auth.models import User
from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    username = factory.Faker("user_name")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if create and extracted:
            self.product.set(extracted)
