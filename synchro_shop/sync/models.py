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
    gtin = models.CharField("Global Trade Identification Number", max_length=255)
    expiry_date = models.DateField()
    reading_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        existing_obj = ShopReading.objects.filter(
            shop=self.shop, gtin=self.gtin
        ).first()
        if existing_obj:
            self.pk = existing_obj.pk
            if self.reading_time < existing_obj.reading_time:
                self.expiry_date = existing_obj.expiry_date
                self.reading_time = existing_obj.reading_time
            return super().save(force_update=True)
        return super().save(*args, **kwargs)
