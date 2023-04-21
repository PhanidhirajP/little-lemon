from django.urls import path
from .views import index, MenuView, SingleItemMenuView

urlpatterns = [
    path("", index),
    path("menu", MenuView.as_view()),
    path("menu/<int:pk>", SingleItemMenuView.as_view()),
]
