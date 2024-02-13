from django import forms

class TrackParcelForm(forms.Form):
    tracking_number = forms.CharField(label='Enter Tracking Number', max_length=100)



class UpdateDeliveryDateForm(forms.Form):
    new_delivery_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


