from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import index, MenuView, SingleItemMenuView

urlpatterns = [
    path("", index),
    path("menu", MenuView.as_view()),
    path("menu/<int:pk>", SingleItemMenuView.as_view()),
    path("token-auth", obtain_auth_token)
]
