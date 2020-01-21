from django import forms

from .models import *



class BusinessForm(forms.ModelForm):

    class Meta:

        model = Business

        fields = ['name', 'neibourhood', 'bizpic', 'biz_email']

        

class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        exclude = ['user']