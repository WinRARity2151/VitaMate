from .models import Pressure_Data
from django.forms import ModelForm

class Pressure_Data_form(ModelForm):
    class Meta:
        model = Pressure_Data
        fields = ['systolic_pressure','diastolic_pressure','pulse']
