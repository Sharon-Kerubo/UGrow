import os
from django.contrib.gis.utils import LayerMapping
from .models import SoilPH

soilph_mapping = {
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'ken2_field': 'KEN2_',
    'suid': 'SUID',
    'phaq': 'PHAQ',
    'phkc': 'PHKC',
    'geom': 'MULTIPOLYGON',
}

soilph_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/ken_soil_ph/ken_soil_ph.shp'))

def run(verbose=True):
    lm = LayerMapping(SoilPH, soilph_shp, soilph_mapping, transform=False, encoding='iso-8859-1')
    lm.save(verbose=True, strict=True)
