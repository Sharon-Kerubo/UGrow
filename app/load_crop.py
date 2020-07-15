import os
from django.contrib.gis.utils import LayerMapping
from .models import crop

crop_mapping = {
    'crops': 'Crops',
    'main_crop': 'Main_Crop',
    'other_crop': 'Other_Crop',
    'county_nam': 'County_Nam',
    'watering': 'Watering',
    'area_km2': 'Area_Km2',
    'geom': 'MULTIPOLYGON',
}

crop_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/kenya_croplands_2015/kenya_croplands_2015.shp'))

def run(verbose=True):
    lm = LayerMapping(crop, crop_shp, crop_mapping, transform=False, encoding='iso-8859-1')
    lm.save(verbose=True, strict=True)
