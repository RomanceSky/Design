from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory

# Using the standard ReuqestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes', {'title': 'new idea'})



