from rest_framework import serializers

from company.models import Company, Works


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
    works = WorksSerializer(required = False, many = True)

    class Meta:
        model = Company
        fields = "__all__"
