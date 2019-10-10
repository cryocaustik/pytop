from rest_framework import serializers
from api.models import Proc


class ProcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proc
        fields = [
            "pid",
            "name",
            "mem",
            "cpu",
            "disk",
            "gpu",
            "network",
            "modified_at",
            "created_at",
        ]
