from django.db import models


class ModelMaster(models.Model):
    is_active = models.BooleanField(default=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # verbose_name_plural = "Master"


class Country(ModelMaster):
    country_name = models.CharField(max_length=50, null=True)
    country_description = models.TextField()
    country_code = models.CharField(max_length=3, null=True)
    currency_symbol = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Country Master"

    def __str__(self):
        return self.country_name


class State(ModelMaster):
    state_name = models.CharField(max_length=50, null=True)
    state_description = models.TextField()
    country_details = models.ForeignKey(Country, on_delete=models.PROTECT,
                                        null=True, related_name="country_details")
    state_code = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        verbose_name_plural = "State Master"

    def __str__(self):
        return self.state_name


class City(ModelMaster):
    city_name = models.CharField(max_length=50, null=True)
    city_description = models.TextField(null=True, blank=True)
    state_details = models.ForeignKey(State, on_delete=models.PROTECT, null=True, related_name="state_details")
    city_code = models.CharField(max_length=5, null=True, blank=True)
    city_pincode = models.CharField(max_length=6, null=True, blank=True)
    city_latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    city_longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name_plural = "City Master"

    def __str__(self):
        return self.city_name


class GstSchemeMaster(ModelMaster):
    gst_scheme_name = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Gst Scheme Master"

    def __str__(self):
        return self.gst_scheme_name


