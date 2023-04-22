from django.test import Client, TestCase
from django.urls import reverse
from django.core import serializers

from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setup(self):
        self.client = Client()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=100, inventory=100)
        Menu.objects.create(title="Chocolate", price=50, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse("menu"))
        expected_data = serializers.serialize("json", Menu.objects.all())
        self.assertJSONEqual(response.content, expected_data)
