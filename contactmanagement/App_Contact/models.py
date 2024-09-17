from django.db import models

# Create your models here.

class ContactBook(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    phone=models.CharField( max_length=50)
    address=models.TextField()
    
    def __str__(self):
        return self.first_name
    