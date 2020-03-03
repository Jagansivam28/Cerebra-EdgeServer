from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from Detections.models import Camera
from django.core import serializers


class getMonitoringDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        camera_id = request.data.get("camera_id")
        if Camera.objects.filter(camera_id=camera_id).exists():
            camera = Camera.objects.get(camera_id=camera_id)
            events_obj = camera.events.all()
            camera_config = {
                "ip_address": camera.ip_address,
                "username": camera.username,
                "password": camera.password,
            }
            detection = []
            for event in events_obj:
                e = {
                    'event_name': event.event_name,
                    'event_category': event.event_category,
                    'model_name': event.model_name,
                    'model_version': event.model_version,
                }
                detection.append(e)

            data = {"camera_config": camera_config, "detections": detection}
            return Response(data)
        else:
            camera = Camera.objects.create()
            events = camera.objects.events()
            camera_config = serializers.serialize("json", camera)
            data = {"camera_config": camera_config, "detections": events}
            return Response(data)
