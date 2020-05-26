from django.contrib import admin
from .models import ShippingCountry

# Register your models here.


class ShippingCountryAdmin(admin.ModelAdmin):
	'''
		Admin View for ShippingCountry
	'''
	list_display = ('country','available','price')


admin.site.register(ShippingCountry, ShippingCountryAdmin)


# class ShippingStationAdmin(admin.ModelAdmin):
#     '''
#         Admin View for ShippingStation
#     '''
#     list_display = ('country','station','price')
#     list_filter = ('station', 'country')
#     list_editable = ('price', 'station',)
#
#
# admin.site.register(ShippingStation, ShippingStationAdmin)