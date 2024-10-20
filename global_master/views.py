from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Country, State, GstSchemeMaster
from .serializers import (CountrySerializer,
                          StateSerializer, GstSchemeMasterSerializer
                          )
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated


class CountryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated,]
    # filterset_fields = ['country_name', 'country_code']
    # search_fields = ['country_name', 'country_code']
    # ordering_fields = ['country_name',]



class StateView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated,]
    # filterset_fields = ['country_name', 'country_code']
    # search_fields = ['country_name', 'country_code']
    # ordering_fields = ['country_name',]


class GstSchemeMasterView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GstSchemeMaster.objects.all()
    serializer_class = GstSchemeMasterSerializer
    permission_classes = [IsAuthenticated,]
    # filterset_fields = ['country_name', 'country_code']
    # search_fields = ['country_name', 'country_code']
    # ordering_fields = ['country_name',]

