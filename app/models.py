from django.contrib.gis.db import models
from django import forms

class crops(models.Model):
    name = models.CharField(max_length=250)
    area = models.CharField(max_length=250)

    def __str__(self):
        return self.name + '_' + self.area

class signup(models .Model):
    username = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
class Counties(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
