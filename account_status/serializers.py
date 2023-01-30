from rest_framework import serializers
from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Status
        fields = "__all__"