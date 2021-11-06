from factory import Faker
from factory.django import DjangoModelFactory

from synchro_shop.sync.models import Shop


class ShopFactory(DjangoModelFactory):

    name = Faker("name")

    class Meta:
        model = Shop
        django_get_or_create = ["name"]
