from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.views import Response

from company.models import Company, Ticket, Works
from company.serializers import CompanySerializer, TicketCreateSerializer, TicketSerializer, WorksSerializer
from user.models import BaseUser


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

    @action(methods=["POST"], detail=True, url_path="give-points")
    def give_points(self, request, *args, **kwargs):
        user = BaseUser.objects.get(id=request.data["user_id"])
        user.points += self.get_object().pointsToGive
        print(self.get_object().pointsToGive, user.points)
        user.save()
        return Response({"ok"})


@extend_schema(tags=["Ticket"])
class TicketView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"status": ["in"], "work": ["in"], "applicant": ["in"]}

    def get_serializer_class(self):
        if self.action == "list":
            return TicketSerializer
        return TicketCreateSerializer
