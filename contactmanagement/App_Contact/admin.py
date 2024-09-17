from django.contrib import admin

# Register your models here.
from .models import ContactBook

admin.site.register(ContactBook)