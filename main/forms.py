from django import forms
from .models import *

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'text-box',
                                                 'placeholder': 'Ваше имя',
                                                 'onfocus': 'blurEvent(this)',
                                                 'onkeyup': 'onChangeEvent(this)',
                                                 'id': 'name'})
        self.fields['from_email'].widget.attrs.update({'class': 'text-box',
                                                       'placeholder': 'Электронная почта',
                                                       'onfocus': 'blurEvent(this)',
                                                       'onkeyup': 'onChangeEvent(this)',
                                                       'id': 'email'})
        self.fields['name'].label = False
        self.fields['from_email'].label = False