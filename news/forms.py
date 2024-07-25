from news.models import ContactUs
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('first_name','last_name','email','phone','message')

