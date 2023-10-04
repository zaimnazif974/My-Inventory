from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        self.item = Item.objects.create(
            name='Test Item',
            ammount = 10,
            description = "test item",
            )
        
    def test_Item_creation(self):
        self.assertEqual(self.item.name,"Test Item" )
        self.assertEqual(self.item.ammount, 10)
        self.assertEqual(self.item.description,"test item")

    def test_default_values(self):
        self.assertEqual(self.item.category, 'Unknown')
        self.assertEqual(self.item.effect, 'None')