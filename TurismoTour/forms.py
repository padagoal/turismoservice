from django import forms
from .models import *


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'


class TourReservaForm(forms.ModelForm):
    class Meta:
        model = TourReserva
        fields = '__all__'