from django.db.models import Count
from rest_framework import viewsets
from rest_framework.views import Response
from api.serializers import ProcSerializer
from api.models import Proc


class ProcViewSet(viewsets.ModelViewSet):
    queryset = Proc.objects.all().order_by("-created_at")
    serializer_class = ProcSerializer

    def get_queryset(self):
        query = {}
        name = self.request.query_params.get("name", None)
        if name:
            query["name"] = name
        return Proc.objects.filter(**query)


class TrackedProcView(viewsets.ModelViewSet):
    queryset = Proc.objects.all().order_by("-created_at")
    serializer_class = ProcSerializer
    http_method_names = ["get"]

    def list(self, request, format=None):
        return Response(Proc.objects.values("name").annotate(dcount=Count("id")))

