from django.test import TestCase
from .forms import ProductForm
from .models import Product
#import hashlib



# Create your tests here.
class FirstTest(TestCase):

# тест на использование шаюлона 
    def test_temple(self):
        response = self.client.get("/jobs/mymenu/singup")
        self.assertTemplateUsed(response, "menu/reg.html")

# тест на возращение формы        
    def test_form(self):
        form = ProductForm(data={"name":"UnittestProduct"})
        self.assertTrue(form.is_valid())
    

  