from django.contrib import admin
from .models import Counties, Soils
from leaflet.admin import LeafletGeoAdmin

class CountiesAdmin(LeafletGeoAdmin):
    list_display = ('county', 'objectid')

class SoilsAdmin(LeafletGeoAdmin):
    list_display = ('soil', 'area')

admin.site.register(Counties, CountiesAdmin)
admin.site.register(Soils, SoilsAdmin)




