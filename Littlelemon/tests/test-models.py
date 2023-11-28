from django.test import TestCase

from Restaurant.models import MenuTable

class MenuTest(TestCase):
    def test_menu(self):
        item = MenuTable.objects.create(title='TestFood', price=10, inventory=10)
        self.assertEqual(item, "TestFood : 10.00")