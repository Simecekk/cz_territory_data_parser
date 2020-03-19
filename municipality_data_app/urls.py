from django.urls import path, include
from .views import ObecAPIView, PouAPIView, OrpAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'obec', ObecAPIView, basename="obec")
router.register(r'pou', PouAPIView, basename="pou")
router.register(r'orp', OrpAPIView, basename="orp")

urlpatterns = [
    path('show/', include(router.urls)),
]