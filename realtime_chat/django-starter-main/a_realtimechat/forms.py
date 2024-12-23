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
        
class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'placeholder': 'Add Name...',
                'class': 'w-full rounded-xl bg-gray-700 text-white px-4 py-2 focus:outline-none',
                'maxlength': '300',
                'autofocus': True,
            }),
        }
