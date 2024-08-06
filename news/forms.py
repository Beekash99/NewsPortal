from news.models import ContactUs, Subscribe, News
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('first_name','last_name','email','phone','message')

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ("email",)

class AddNewsByReporterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category']. empty_label= "select your category"
    class Meta:
        model = News
        fields = ("title","category","image","description")


class updateNewsByReporterForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ("title","category","image","description")