from django.db import models

class Camera(models.Model):
    IP_ADDRESS="192.168.33.11"
    USERNAME="ADMIN"
    PASSWORD="ADMIN"
    CAMERA_ID="453"
    camera_id=models.CharField(max_length=20,default=CAMERA_ID,null=True,blank=True)
    ip_address=models.CharField(max_length=13,default=IP_ADDRESS,null=True,blank=True)
    username=models.CharField(max_length=25,default=USERNAME,null=True,blank=True)
    password=models.CharField(max_length=15,default=PASSWORD,null=True,blank=True)


    def __str__(self):
        return "username = {} , ip= {}".format(self.USERNAME,self.PASSWORD)


class Event_Coordinates(models.Model):
     x1=models.FloatField(null=True,blank=True)
     x2 = models.FloatField(null=True, blank=True)
     y1 = models.FloatField(null=True, blank=True)
     y2 = models.FloatField(null=True, blank=True)


class Event(models.Model):
    HARD_HAT=0
    SAFETY_VEST=1
    GOGGLES=2
    GLOVES=3
    SHOES=4
    RESTRICTED_ENTRY=5
    MOBILE_PHONE_USAGE=6
    FIRE=7
    OIL_SPILL=8
    EVENT_CHOICES=[
        (HARD_HAT,"Hard hat"),
        (SAFETY_VEST,"Safety Vest"),
        (GOGGLES,'Googles'),
        (GLOVES,'Gloves'),
        (SHOES,'Shoes'),
        (RESTRICTED_ENTRY,"Restricted Entry"),
        (MOBILE_PHONE_USAGE,"Mobile Phone Usage"),
        (FIRE,"Fire"),
        (OIL_SPILL,"Oil Spill")
    ]

    SAFETY=0
    RESTRICTIONS=1

    EVENT_CATEGORY_CHOICES=[
        (RESTRICTIONS,"Restrictions"),
        (SAFETY,"Safety")
    ]
    ou_id=models.ForeignKey(Camera,on_delete=models.CASCADE,related_name="events",null=True,blank=True)
    event_name=models.IntegerField(max_length=2,choices=EVENT_CHOICES,null=True,blank=True)
    event_category=models.IntegerField(max_length=2,choices=EVENT_CATEGORY_CHOICES,null=True,blank=True)
    model_name=models.CharField(max_length=20,null=True,blank=True)
    model_version=models.CharField(max_length=10,null=True,blank=True)
    confidence_score=models.BooleanField(null=True,blank=True)
    event_coordinates=models.ForeignKey(Event_Coordinates,on_delete=models.CASCADE,related_name="coordinates",null=True,blank=True)
    event_state=models.BooleanField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)







