from django.urls import path
from .views import register_user, login_user, logout


urlpatterns = [
    path('register_user/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout, name="logout"),
]
