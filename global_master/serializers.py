from rest_framework import serializers
from .models import Country, State, GstSchemeMaster


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "country_name", "country_description", "country_code", "currency_symbol",
                  "is_active", "is_deleted"]


class StateSerializer(serializers.ModelSerializer):
    country_details = CountrySerializer(read_only=True)

    class Meta:
        model = State
        fields = ["id", "state_name", "state_description", "country_details", "state_code",
                  "is_active", "is_deleted"]


class GstSchemeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GstSchemeMaster
        fields = ["id", "gst_scheme_name", "description", "is_active", "is_deleted"]

