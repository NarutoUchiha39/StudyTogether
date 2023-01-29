from django.db import models
from django.contrib.auth.models import User 

class topic(models.Model):
    description = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.description
class Room(models.Model):
    name = models.CharField(max_length=100)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.ForeignKey(topic,on_delete=models.SET_NULL,null=True)
    Date_Created = models.DateField(auto_now_add=True)
    #participants =
    description = models.CharField(max_length=100,null=True,blank=True)
    updated = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-updated','-Date_Created']

class messages(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    Date_Created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.body[:50]



