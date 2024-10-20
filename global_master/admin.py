from django.contrib import admin
from .models import *

class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name", "country_code", "currency_symbol", "is_active", "is_deleted")
    search_fields = ("country_name", "country_code")
    readonly_fields = ('created_at', 'updated_at')


class StateAdmin(admin.ModelAdmin):
    list_display = ("state_name", "state_code", "is_active", "is_deleted")
    search_fields = ("state_name", "state_code")
    readonly_fields = ('created_at', 'updated_at')


class CityAdmin(admin.ModelAdmin):
    list_display = ("city_name", "city_code", "city_pincode", "is_active", "is_deleted")
    search_fields = ("city_name", "city_code", "city_pincode")
    readonly_fields = ('created_at', 'updated_at')


class GstSchemeMasterAdmin(admin.ModelAdmin):
    list_display = ("gst_scheme_name", "is_active", "is_deleted")
    search_fields = ("gst_scheme_name",)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(GstSchemeMaster, GstSchemeMasterAdmin)
# admin.site.register()
# admin.site.register()
