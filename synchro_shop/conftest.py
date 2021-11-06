import pytest

from synchro_shop.sync.models import Shop
from synchro_shop.sync.tests.factories import ShopFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def shop() -> Shop:
    return ShopFactory()
