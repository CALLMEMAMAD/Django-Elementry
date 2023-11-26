from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
   def test_url_exists_at_correct_location(self):
       response = self.client.get("/")
       self.assertEqual(response.status_code, 200)

class AboutpageTests(SimpleTestCase):
   def test_url_exists_at_correct_location(self):
       response = self.client.get("/about/")
       self.assertEqual(response.status_code, 200)
  
"""for run this one please type in terminal: python manage.py test """
# Create your tests here.
