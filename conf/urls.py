from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("superadminlogin/", admin.site.urls),
    path("globals/", include("global_master.urls")),
    path("account/", include("accounts.urls")),
    path("v1/api/", include("api.urls")),

]
