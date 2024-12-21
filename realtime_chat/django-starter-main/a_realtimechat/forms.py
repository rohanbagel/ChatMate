from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Type a message...',
                'class': 'w-full rounded-xl bg-gray-700 text-white px-4 py-2 focus:outline-none',
                'maxlength': '300',
                'required': True
            }),
        }