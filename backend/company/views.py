from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from company.models import Company, Works
from company.serializers import CompanySerializer, WorksSerializer


# Create your views here.


@extend_schema(tags=["Company"])
class CompanyListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"employer": ["in"]}


@extend_schema(tags=["Works"])
class WorksListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = WorksSerializer
    queryset = Works.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"company": ["in"]}
