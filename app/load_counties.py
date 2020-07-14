import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

counties_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/kenyan-counties/County.shp'))

def run(verbose=True):
    ls = LayerMapping(Counties, county_shp, counties_mapping, transform=False, encoding='iso-8859-1')
    ls.save(verbose=True, strict=True)
