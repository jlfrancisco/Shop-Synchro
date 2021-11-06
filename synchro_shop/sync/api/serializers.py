from rest_framework import serializers

from synchro_shop.sync.models import ShopReading


class ShopReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopReading
        fields = "__all__"
