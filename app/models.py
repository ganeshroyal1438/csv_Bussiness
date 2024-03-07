from django.db import models

# Create your models here.
class Business(models.Model):
    series_refference=models.CharField(max_length=100)
    period=models.FloatField()
    data_value=models.CharField(max_length=100)
    suppressed=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    units=models.CharField(max_length=100)
    magnitude=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    group=models.CharField(max_length=100)
    series_titel_1=models.CharField(max_length=100)
    series_titel_2=models.CharField(max_length=100)
    series_titel_3=models.CharField(max_length=100)
    series_titel_4=models.CharField(max_length=100)
    series_titel_5=models.CharField(max_length=100)

