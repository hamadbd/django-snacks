from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class ThingsTest(SimpleTestCase):

    def test_home_page(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

    def test_base_temp(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'base.html')


    # About Page
    def test_about_page(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_about_template(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'about.html')
    
