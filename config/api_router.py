from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from synchro_shop.sync.api.views import ShopReadingViewSet
from synchro_shop.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sync", ShopReadingViewSet)


app_name = "api"
urlpatterns = router.urls
