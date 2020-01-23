from django.shortcuts import render
from rest_framework.views import APIView,Response
from rest_framework import permissions
from Detections.models import Camera
from django.core import serializers

class getMonitoringDetails(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        camera_id=request.data.get("camera_id")
        if Camera.objects.filter(camera_id=camera_id).exists():
            camera=Camera.objects.get(camera_id=camera_id)
            events=camera.objects.events()
            camera_config= serializers.serialize("json", camera)
            data={"camera_config":camera_config,"detections":events}
            return Response(data)
        else:
            camera=Camera.objects.create()
            events = camera.objects.events()
            camera_config = serializers.serialize("json", camera)
            data = {"camera_config": camera_config, "detections": events}
            return Response(data)
