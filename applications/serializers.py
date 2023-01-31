from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Application
        fields = "__all__"
