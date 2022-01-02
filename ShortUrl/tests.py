from django.test import TestCase, Client
from .models import Url
from django.urls import reverse


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = Url.objects.create( # Create an object to test the redirect of the short url and a made up url.
            original_url = "https://he.wikipedia.org/wiki/%D7%A6%D7%91%D7%A2%D7%99_%D7%97%D7%AA%D7%95%D7%9C%D7%99%D7%9D",
            short_url = "y7yr43er4",
            click_time = 0) 

        self.create_url = reverse("create-page")

        self.redirect_url_pagenotfound = reverse('redirect',args=['rty']) # Sending made up url
        self.redirect_url = reverse('redirect',args=['y7yr43er4']) # Sending the right url      
   
    def test_create(self):
        data = {'original_url': "https://he.wikipedia.org/wiki/%D7%95%D7%95%D7%9E%D7%91%D7%98_%D7%9E%D7%A6%D7%95%D7%99"}
        response = self.client.post(self.create_url, data)
        short_url = Url.objects.get(original_url = "https://he.wikipedia.org/wiki/%D7%95%D7%95%D7%9E%D7%91%D7%98_%D7%9E%D7%A6%D7%95%D7%99").short_url # Get the short url after he has been created 

        self.assertTemplateUsed(response, "ShortUrl/main.html") # Testing the use in the right html page
        self.assertLess(len(short_url), len(data["original_url"]) ) # Testing if the short url is actually short then the original of course if the original url actually need shorcat

  

    def test_redirect(self):
        response_wrong_short_url = self.client.get(self.redirect_url_pagenotfound)
        response_short_url = self.client.get(self.redirect_url)

        self.assertTemplateUsed(response_wrong_short_url, "ShortUrl/pagenotfound.html") # The made up url redirect to pagenotfound html
        self.assertURLEqual(response_short_url.url, self.url.original_url) # The right url redirect to the original url





 

