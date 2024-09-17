from django import forms
from .models import ContactBook

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactBook
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']