from django.contrib import admin
from .models import *


class UnitAdmin(admin.ModelAdmin):
    list_display = ("unit_name", "is_active", "is_deleted")
    search_fields = ("unit_name",)
    readonly_fields = ('created_at', 'updated_at')


class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "is_active", "is_deleted")
    search_fields = ("brand_name",)
    readonly_fields = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "is_active", "is_deleted")
    search_fields = ("category_name",)
    readonly_fields = ('created_at', 'updated_at')


class PartyTypeAdmin(admin.ModelAdmin):
    list_display = ("party_type", "is_active", "is_deleted")
    search_fields = ("party_type",)
    readonly_fields = ('created_at', 'updated_at')


class PartyLedgerAdmin(admin.ModelAdmin):
    list_display = ("party_name", "party_state", "party_mobile_number", "party_type_details", "is_active", "is_deleted")
    search_fields = ("party_name",)
    readonly_fields = ('created_at', 'updated_at')


class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ("product_name", "barcode", "sku_code", "brand_details", "is_active", "is_deleted")
    search_fields = ("product_name", "barcode", "sku_code", "brand_details__brand_name",)
    readonly_fields = ('created_at', 'updated_at')


class ImageMasterAdmin(admin.ModelAdmin):
    # list_display = ("product_details", )
    search_fields = ("product_details__product_name", "product_details__barcode",
                     "product_details__sku_code")
    readonly_fields = ('created_at', 'updated_at')


class HsnMasterAdmin(admin.ModelAdmin):
    list_display = ("hsn_code", "tax_rate", "c_gst", "s_gst", "is_active", "is_deleted")
    search_fields = ("hsn_code", "tax_rate")
    readonly_fields = ('created_at', 'updated_at')


class CustomerMasterAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "mobile_number", "gender", "country_details", "is_active", "is_deleted")
    search_fields = ("customer_name", "mobile_number", "country_details")
    readonly_fields = ('created_at', 'updated_at')


class CompanyMasterAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_mobile", "country", "state", "city", "gst_number",
                    "is_active", "is_deleted")
    search_fields = ("gst_scheme_name",)
    readonly_fields = ('created_at', 'updated_at')



admin.site.register(Unit, UnitAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PartyType, PartyTypeAdmin)
admin.site.register(PartyLedger, PartyLedgerAdmin)
admin.site.register(ProductMaster, ProductMasterAdmin)
admin.site.register(ProductsImages, ImageMasterAdmin)
admin.site.register(HsnMaster, HsnMasterAdmin)
admin.site.register(CustomerMaster, CustomerMasterAdmin)
admin.site.register(CompanyMaster, CompanyMasterAdmin)
# admin.site.register()
# admin.site.register()
# admin.site.register()
