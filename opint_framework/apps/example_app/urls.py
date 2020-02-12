from django.urls import path, include
from rest_framework import routers
from .api.views import SampleViewSet

router = routers.DefaultRouter()
router.register(r'sample_api', SampleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]