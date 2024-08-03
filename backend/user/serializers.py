from rest_framework import serializers
from user.models import BaseUser

class userMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = "__all__"