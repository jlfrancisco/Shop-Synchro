import pytest

from synchro_shop.sync.models import Shop
from synchro_shop.sync.tests.factories import ShopFactory
from synchro_shop.users.models import User
from synchro_shop.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture()
def shop() -> Shop:
    return ShopFactory()
