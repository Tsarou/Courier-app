from django import forms
from .models import Parcel
from django.utils import timezone

class UpdateDeliveryDateForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['planned_delivery_date']

    def clean_planned_delivery_date(self):
        planned_delivery_date = self.cleaned_data['planned_delivery_date']
        if planned_delivery_date <= timezone.now().date():
            raise forms.ValidationError("The planned delivery date must be in the future.")
        return planned_delivery_date
