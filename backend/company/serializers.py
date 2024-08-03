from rest_framework import serializers

from company.models import Company, Ticket, Works
from user.models import BaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["id", "name", "email", "points"]


class CompanyTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class WorksSerializer(serializers.ModelSerializer):
    company = CompanyTwoSerializer()

    class Meta:
        model = Works
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    works = WorksSerializer(required=False, many=True)

    class Meta:
        model = Company
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    work = WorksSerializer()
    applicant = UserSerializer()

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
