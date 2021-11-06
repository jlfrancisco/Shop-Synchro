from datetime import datetime, timezone

import pytest

from synchro_shop.sync.models import Shop, ShopReading

pytestmark = pytest.mark.django_db

GTIN = "GLOBAL TRADE ID NUMBER"


def test_new_shopreading_save(shop: Shop):
    date1 = datetime.fromisoformat("2021-11-05 11:56").replace(tzinfo=timezone.utc)
    exp1 = datetime.fromisoformat("2022-08-05").replace(tzinfo=timezone.utc)
    date2 = datetime.fromisoformat("2021-11-06 13:12").replace(tzinfo=timezone.utc)
    exp2 = datetime.fromisoformat("2022-07-25").replace(tzinfo=timezone.utc)
    bef = ShopReading.objects.create(
        shop=shop, gtin=GTIN, expiry_date=exp1, reading_time=date1
    )
    aft = ShopReading.objects.create(
        shop=shop, gtin=GTIN, expiry_date=exp2, reading_time=date2
    )

    assert bef.pk == aft.pk
    assert aft.expiry_date == exp2


def test_old_shopreading_save(shop: Shop):
    date1 = datetime.fromisoformat("2021-11-05 11:56").replace(tzinfo=timezone.utc)
    exp1 = datetime.fromisoformat("2022-08-05").replace(tzinfo=timezone.utc)
    date2 = datetime.fromisoformat("2021-11-04 16:12").replace(tzinfo=timezone.utc)
    exp2 = datetime.fromisoformat("2022-09-25").replace(tzinfo=timezone.utc)
    bef = ShopReading.objects.create(
        shop=shop, gtin=GTIN, expiry_date=exp1, reading_time=date1
    )
    aft = ShopReading.objects.create(
        shop=shop, gtin=GTIN, expiry_date=exp2, reading_time=date2
    )

    assert bef.pk == aft.pk
    assert aft.expiry_date == exp1.date()
