from django.forms import ModelForm

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
