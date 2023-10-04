from django.db import models
from datetime import time

class Pressure_Data(models.Model):
    systolic_pressure = models.IntegerField()
    diastolic_pressure = models.IntegerField()
    pulse = models.IntegerField()
    date = models.DateField(auto_now_add=True, editable=False)
    time = models.TimeField(auto_now_add=True, editable=False)


