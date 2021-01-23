from django import forms
from .models import ReservasHotel


class ReservaHotelForm(forms.ModelForm):
    class Meta:
        model = ReservasHotel
        fields = '__all__'