from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Ice Cream", price=80.00, inventory=100)
        self.item2 = Menu.objects.create(title="Cake", price=120.00, inventory=50)
        self.item3 = Menu.objects.create(title="Pizza", price=250.00, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # Make sure this matches your router's name
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        