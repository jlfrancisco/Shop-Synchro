import uuid

from django.db import models


class Shop(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ShopReading(models.Model):
    shop = models.ForeignKey(
        Shop, related_name="shop_reading", on_delete=models.CASCADE
    )
    gtin = models.CharField(
        "Global Trade Identificationn Number", max_length=255, unique=True
    )
    expiry_date = models.DateField()
    reading_time = models.DateTimeField()
