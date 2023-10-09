from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from treasures.models import Treasure

# Create your tests here.

class TreasureAPITestCase(TestCase):
    def setUp(self):
        self.treasure= Treasure.objects.create(name='Test Treasure', price=76.99)
        self.treasure_list_url = reverse('treasures:treasure-list')
        self.treasure_detail_url = reverse('treasures:treasure-detail', args=[self.treasure.pk])

    def test_get_all_treasure(self):
        response = self.client.get(self.treasure_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_treasure(self):
        response = self.client.get(self.treasure_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_treasure(self):
        data = {'name': 'New treasure', 'price': 35.99}
        response = self.client.post(self.treasure_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_treasure(self):
        data = {'name': 'Updated Treasure', 'price': 95.99}
        response = self.client.put(self.treasure_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_treasure(self):
        response = self.client.delete(self.treasure_list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)