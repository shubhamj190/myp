from django import forms
from django.forms import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=["name","email","contact", "subject", "message"]
