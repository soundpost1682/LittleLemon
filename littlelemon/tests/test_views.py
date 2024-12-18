from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        appiti = Menu.objects.create(title='appiti', price=8.5, iventory=10)
        babo = Menu.objects.create(title='babo', price=5.00, inventory=20)
    
    def test_getall(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'appiti')
        self.assertContains(response, 'babo')
        