from django.urls import path
from Detections.views import *

urlpatterns = [
    path('/getMonitoringDetails',getMonitoringDetails),
]