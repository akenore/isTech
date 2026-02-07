from django import forms
from public.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email Address'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter Number +17745431743'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Enter Subject'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Enter message'})

