from rest_framework import routers

from .views import TranslateViewSet, WordViewSet

router = routers.DefaultRouter()
router.register("word", WordViewSet)
router.register("translate", TranslateViewSet)


urlpatterns = router.urls
