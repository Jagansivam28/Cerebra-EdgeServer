from django.urls import path
from Detections.views import getMonitoringDetails

urlpatterns = [
    path('getMonitoringDetails', getMonitoringDetails.as_view(), name="getMonitoringDetails"),
]
