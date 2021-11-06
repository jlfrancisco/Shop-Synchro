from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from synchro_shop.sync.models import ShopReading

from .serializers import ShopReadingSerializer


class ShopReadingViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ShopReadingSerializer
    queryset = ShopReading.objects.all()
    permission_classes = [AllowAny]
