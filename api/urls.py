from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api.views import ProcViewSet, TrackedProcView

router = routers.DefaultRouter()
router.register("usage", ProcViewSet)
router.register("proc", TrackedProcView, base_name="procs")

urlpatterns = [
    # url("proc", TrackedProcView.as_view()),
    path("", include(router.urls))
]
