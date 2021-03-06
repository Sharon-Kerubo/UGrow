from django.contrib.gis.db import models
from django import forms

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

class Soils(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    ilrifnl_field = models.FloatField()
    suid = models.FloatField()
    bedr = models.FloatField()
    sdra = models.CharField(max_length=254, null=True)
    sdra_descr = models.CharField(max_length=254, null=True)
    prop = models.IntegerField()
    prid = models.CharField(max_length=254, null=True)
    phaq = models.FloatField()
    phkc = models.FloatField()
    exna = models.FloatField()
    exck = models.FloatField()
    cecs = models.FloatField()
    drai = models.CharField(max_length=254, null=True)
    drai_descr = models.CharField(max_length=254, null=True)
    rdep = models.CharField(max_length=254,null=True)
    rdep_descr = models.CharField(max_length=254, null=True)
    lith = models.CharField(max_length=254, null=True)
    slop = models.IntegerField()
    reli = models.IntegerField()
    soil = models.CharField(max_length=254, null=True)
    sid = models.IntegerField()
    clay = models.CharField(max_length=254, null=True)
    clay_descr = models.CharField(max_length=254, null=True)
    text = models.CharField(max_length=254, null=True)
    text_descr = models.CharField(max_length=254, null=True)
    rslo = models.CharField(max_length=254, null=True)
    rslo_descr = models.CharField(max_length=254, null=True)
    lndf = models.CharField(max_length=254, null=True)
    lndf_descr = models.CharField(max_length=254, null=True)
    geom = models.MultiPolygonField(srid=4326)

class SoilPH(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    ken2_field = models.FloatField()
    suid = models.FloatField()
    phaq = models.FloatField()
    phkc = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

class Temperature(models.Model):
    area = models.ForeignKey(Counties, default=1, on_delete=models.SET_DEFAULT)
    element = models.CharField(max_length=254, null=True)
    jan = models.CharField(max_length=254, null=True)
    feb = models.CharField(max_length=254, null=True)
    mar = models.CharField(max_length=254, null=True)
    apr = models.CharField(max_length=254, null=True)
    may = models.CharField(max_length=254, null=True)
    jun = models.CharField(max_length=254, null=True)
    jul = models.CharField(max_length=254, null=True)
    aug = models.CharField(max_length=254, null=True)
    sep = models.CharField(max_length=254, null=True)
    oct = models.CharField(max_length=254, null=True)
    nov = models.CharField(max_length=254, null=True)
    dec = models.CharField(max_length=254, null=True)

class Humidity(models.Model):
    area = models.ForeignKey(Counties, default=1, on_delete=models.SET_DEFAULT)
    element = models.CharField(max_length=254, null=True)
    jan = models.CharField(max_length=254, null=True)
    feb = models.CharField(max_length=254, null=True)
    mar = models.CharField(max_length=254, null=True)
    apr = models.CharField(max_length=254, null=True)
    may = models.CharField(max_length=254, null=True)
    jun = models.CharField(max_length=254, null=True)
    jul = models.CharField(max_length=254, null=True)
    aug = models.CharField(max_length=254, null=True)
    sep = models.CharField(max_length=254, null=True)
    oct = models.CharField(max_length=254, null=True)
    nov = models.CharField(max_length=254, null=True)
    dec = models.CharField(max_length=254, null=True)

class Rainfall(models.Model):
    area = models.ForeignKey(Counties, default=1, on_delete=models.SET_DEFAULT)
    element = models.CharField(max_length=254, null=True)
    jan = models.CharField(max_length=254, null=True)
    feb = models.CharField(max_length=254, null=True)
    mar = models.CharField(max_length=254, null=True)
    apr = models.CharField(max_length=254, null=True)
    may = models.CharField(max_length=254, null=True)
    jun = models.CharField(max_length=254, null=True)
    jul = models.CharField(max_length=254, null=True)
    aug = models.CharField(max_length=254, null=True)
    sep = models.CharField(max_length=254, null=True)
    oct = models.CharField(max_length=254, null=True)
    nov = models.CharField(max_length=254, null=True)
    dec = models.CharField(max_length=254, null=True)

class crops(models.Model):
    name = models.CharField(max_length=254, null=True)
    rainfall = models.CharField(max_length=254, null=True)
    ph = models.CharField(max_length=254, null=True)
    temperature = models.CharField(max_length=254, null=True)
    humidity = models.CharField(max_length=254, null=True)
    drainage = models.CharField(max_length=254, null=True)

class crop(models.Model):
    crops = models.CharField(max_length=254, null=True)
    main_crop = models.CharField(max_length=254, null=True)
    other_crop = models.CharField(max_length=254, null=True)
    county_nam = models.CharField(max_length=254, null=True)
    watering = models.CharField(max_length=254, null=True)
    area_km2 = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
