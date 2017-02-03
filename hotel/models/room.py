from django.db import models

from hotel.models.hotel import Hotel

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    ctrip_id = models.IntegerField()