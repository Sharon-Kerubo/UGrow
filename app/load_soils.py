import os
from django.contrib.gis.utils import LayerMapping
from .models import Soils

soils_mapping = {
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'ilrifnl_field': 'ILRIFNL_',
    'suid': 'SUID',
    'bedr': 'BEDR',
    'sdra': 'SDRA',
    'sdra_descr': 'SDRA_DESCR',
    'prop': 'PROP',
    'prid': 'PRID',
    'phaq': 'PHAQ',
    'phkc': 'PHKC',
    'exna': 'EXNA',
    'exck': 'EXCK',
    'cecs': 'CECS',
    'drai': 'DRAI',
    'drai_descr': 'DRAI_DESCR',
    'rdep': 'RDEP',
    'rdep_descr': 'RDEP_DESCR',
    'lith': 'LITH',
    'slop': 'SLOP',
    'reli': 'RELI',
    'soil': 'SOIL',
    'sid': 'SID',
    'clay': 'CLAY',
    'clay_descr': 'CLAY_DESCR',
    'text': 'TEXT',
    'text_descr': 'TEXT_DESCR',
    'rslo': 'RSLO',
    'rslo_descr': 'RSLO_DESCR',
    'lndf': 'LNDF',
    'lndf_descr': 'LNDF_DESCR',
    'geom': 'MULTIPOLYGON',
}

soils_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/soils/soils.shp'))

def run(verbose=True):
    lm = LayerMapping(Soils, soils_shp, soils_mapping, transform=False, encoding='iso-8859-1')
    lm.save(verbose=True, strict=True)
