from global_master.models import (
    ModelMaster, Country,
    State, City, GstSchemeMaster
)
import uuid
from django.db import models
# from django.contrib.auth.models import User
from accounts.models import CustomUser as User


def create_unique_barcode():
    return str(uuid.uuid4().int)[:10]


class CompanyMaster(ModelMaster):
    # company details
    user = models.ForeignKey(User, related_name="company_user", on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100, blank=False, null=True)
    company_alias = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    company_mobile = models.CharField(max_length=13, blank=False, null=True)
    company_phone_number = models.CharField(max_length=13, blank=False, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    company_address1 = models.CharField(max_length=250, blank=True, null=True)
    company_address2 = models.CharField(max_length=250, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=False)
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=False)
    city = models.CharField(max_length=40, null=True, blank=False)
    company_pincode = models.CharField(max_length=6, blank=True, null=True)

    fy_starts = models.DateField(blank=False, null=True)    
    currency_symbol = models.CharField(max_length=4, null=True, default="₹")
    formal_currency_name = models.CharField(max_length=5, blank=True, null=True)
    is_stock_maintained = models.BooleanField(default=True, null=True)
    
    is_vat_enabled = models.BooleanField(default=False, null=True)
    vat_number = models.CharField(max_length=15, blank=True, null=True)
    is_gst_enabled = models.BooleanField(default=False, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    gst_scheme = models.ForeignKey(GstSchemeMaster, null=True, on_delete=models.PROTECT)
    opening_balance = models.DecimalField(decimal_places=3, blank=True, max_digits=20)
    company_pan_number = models.CharField(max_length=10, blank=True, null=True)
    company_tin_number = models.CharField(max_length=25, null=True, blank=True)

    company_bank_acct_holder_name = models.CharField(max_length=100, blank=True, null=True)
    company_bank_name = models.CharField(max_length=50, blank=True, null=True)
    company_bank_account_number = models.CharField(max_length=30, blank=True, null=True)
    company_bank_ifsc_code = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Company Master"

    def __str__(self):
        return self.company_name


class Unit(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="unit_company")
    unit_name = models.CharField(max_length=50, null=True)
    unit_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Unit Master"

    def __str__(self):
        return self.unit_name


class Brand(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="brand_company")
    brand_name = models.CharField(max_length=50, null=True)
    brand_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Brand Master"

    def __str__(self):
        return self.brand_name


class Category(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="category_company")
    category_name = models.CharField(max_length=50, null=True)
    category_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Category Master"

    def __str__(self):
        return self.category_name


class HsnMaster(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="hsn_company")
    hsn_code = models.CharField(max_length=10, null=True)
    hsn_description = models.TextField()
    tax_rate = models.DecimalField(max_digits=5, decimal_places=3)
    c_gst = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    s_gst = models.DecimalField(max_digits=5, decimal_places=3, null=True)

    class Meta:
        verbose_name_plural = "HSN Master"

    def __str__(self):
        return f"{self.hsn_code}"


class PartyType(ModelMaster):
    # Sundry Creditors, sundry Debtors etc.
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="party_type_company")
    party_type = models.CharField(max_length=100, null=True)
    party_type_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Party Type Master"

    def __str__(self):
        return self.party_type


class PartyLedger(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="party_ledger_company")
    party_name = models.CharField(max_length=100)
    party_alias = models.CharField(max_length=50, blank=True, null=True)
    party_address = models.TextField(null=True, blank=True)
    party_state = models.ForeignKey(State, on_delete=models.PROTECT, null=True)
    party_phone_number = models.CharField(max_length=13, null=True, blank=True)
    party_mobile_number = models.CharField(max_length=13, null=True, blank=True)
    party_email = models.EmailField(null=True, blank=True)
    party_gst_number = models.CharField(max_length=15, null=True, blank=True)
    party_type_details = models.ForeignKey(PartyType, on_delete=models.PROTECT,
                                           related_name="party_type_details")
    opening_balance = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        verbose_name_plural = "Party Master"

    def __str__(self):
        return self.party_name


class ProductMaster(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True, related_name="product_master_company")
    product_name = models.CharField(max_length=100, null=True)
    product_description = models.TextField(null=True, blank=True)
    brand_details = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True,
                                      related_name="brand_details")
    category_details = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True,
                                         related_name="category_details")
    unit_details = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True,
                                     related_name="unit_details")
    barcode = models.CharField(max_length=20, blank=True, null=True, default=create_unique_barcode)
    sku_code = models.CharField(max_length=20, null=True, blank=True, default=create_unique_barcode)
    hsn_details = models.ForeignKey(HsnMaster, on_delete=models.PROTECT, null=True, blank=True,
                                    related_name="hsn_details")
    thumbnail = models.ImageField(upload_to="products_images/", null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(null=True, blank=True, max_length=20)

    class Meta:
        verbose_name_plural = "Product Master"
        indexes = [
            models.Index(fields=['product_name', 'barcode', 'sku_code']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['company', 'barcode'], name='unique_company_barcode'),
            models.UniqueConstraint(fields=['company', 'sku_code'], name='unique_company_sku_code'),
        ]

    def __str__(self):
        return self.product_name


class ProductsImages(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True,
                                related_name="product_images_company")
    product_details = models.ForeignKey(ProductMaster, on_delete=models.CASCADE, null=True, blank=True,
                                        related_name="product_images")
    image = models.ImageField(upload_to="products_images/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_details.product_name} - {self.product_details.barcode} -\
                    {self.product_details.sku_code}"


class CustomerMaster(ModelMaster):
    company = models.ForeignKey(CompanyMaster, on_delete=models.PROTECT, null=True,
                                related_name="customer_master_company")
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=13, null=True, blank=False)
    alternate_mobile_number = models.CharField(max_length=13, null=True, blank=False)
    gender = models.CharField(max_length=20, null=True, blank=False,
                              choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    email_address = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    anniversary = models.DateField(null=True, blank=True)
    customer_address = models.TextField(blank=True, null=True)
    country_details = models.ForeignKey(Country, blank=True, null=True, on_delete=models.PROTECT,
                                        related_name="customer_country_details")
    state_details = models.ForeignKey(State, blank=True, null=True, on_delete=models.PROTECT,
                                      related_name="customer_state_details")
    city_details = models.ForeignKey(City, blank=True, null=True, on_delete=models.PROTECT,
                                      related_name="customer_city_details")

    class Meta:
        verbose_name_plural = "Customer Master"

    def __str__(self):
        return self.customer_name


class PurchaseMasterHeader(ModelMaster):
    ...







