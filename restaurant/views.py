from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer

# Create your views here.


def index(request):
    return render(request, "index.html", {})


class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleItemMenuView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
