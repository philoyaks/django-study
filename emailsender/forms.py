from django import forms
from django.db.models import fields

from emailsender.models import EmailModel
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


class EmailMaster(forms.ModelForm):
    class Meta:
        model =EmailModel
        fields =['emailadress', 'fullname']
        
