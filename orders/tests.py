from django.test import TestCase
from django.urls import reverse

class UserTest(TestCase):
    def test_craete_user(self):
        url=reverse('show_address')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_address(self):
        url=reverse('add_address')
        data={
            'name':'shivam',
            'address':'tgyh',
            'apartment_suit':'rftg',
            'city':'fazilka',
            'country':'india',
            'province':'152123',
            'postal':'152123'
        }     
        response=self.client.post(url,data,format='text/html')
        self.assertEqual(response.status_code,302)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        
        
