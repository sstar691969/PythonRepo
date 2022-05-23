
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.DateTimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle


    class Meta:
        db_table='meeting'


class Meeting_Minutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.CharField(max_length=255)
    minutestext=models.TextField()

    def __str__(self):
        return str(self.meetingid)


    class Meta:
        db_table='meeting_minutes'


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.DateField()
    url=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=255)


    def __str__(self):
        return self.resourcename


    class Meta:
        db_table='resource'



class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.DateField()
    date=models.DateField()
    time=models.DateTimeField()
    description=models.TextField(max_length=255)
    userid=models.ManyToManyField(User)


    def discountAmount(self):
        self.discount=self.price * .05
        return self.discount

        #needs work on discount price
        #something to do with the \

    def discountPrice(self):
        disc=self.discountAmount()
        self.discountedPrice=self.price.disc



    def __str__(self):
        return self.eventtitle


    class Meta:
        db_table='event'



    
    


        
    
