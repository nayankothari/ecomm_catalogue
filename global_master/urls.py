from rest_framework import routers
from django.urls import path, include
from .views import CountryView, StateView, GstSchemeMasterView


router = routers.DefaultRouter()
router.register(r"countries", CountryView, basename="country")
router.register(r"states", StateView, basename="state")
router.register(r"gst-schemes", GstSchemeMasterView, basename="gstscheme")

urlpatterns = [
    path("", include(router.urls)),
]
