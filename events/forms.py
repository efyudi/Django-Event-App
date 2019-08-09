from .models import Venue
from django import forms


class VenueForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Venue
        fields = '__all__'

    # a custom validation to check to accept either of user personal details are entered or not
    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        email_address = cleaned_data.get('email_address')

        if not (phone or email_address):
            raise forms.ValidationError(
                "You Must Enter Either a Phone Number or an Email, or Both")
