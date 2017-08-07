from django.forms import ModelForm
from django import forms

from .models import RegistrationRequest

class RegistrationRequestForm(ModelForm):
    class Meta:
        model = RegistrationRequest
        fields = [
            "full_name",
            "title",
            "organization_name",
            "email_address",
            "phone_number",
            "comments"
        ]
        # labels = {
        #     "service_level_token": "UPS Service Level"
        # }
        # widgets = {
        #     'password': forms.PasswordInput()
        # }