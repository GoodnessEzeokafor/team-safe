from django.contrib import admin
# from leaflet.admin import LeafletGeoAdmin
from .models import (
	Incidence,
)
#Register your models here.


class IncidenceAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug','location', 'description', 'created', 'updated')

# class StateAdmin(admin.ModelAdmin):
# 	list_display = ('name_1', 'hasc_1')
    
admin.site.register(Incidence, IncidenceAdmin)
# admin.site.register(State, StateAdmin)


