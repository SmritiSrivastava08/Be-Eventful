from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class customer(models.Model):
    Name = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)

GENDER = [
    ('Female', 'female'),
    ('Male', 'male'),
    ('Others', 'others'),
]

EVENT = [
    ('Wedding', 'wedding'),
    ('Birthday', 'birthday'),
    ('Corporate', 'corporate'),
    ('Social Gathering', 'social gathering'),
]

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    Phone_No = models.IntegerField()
    Address = models.TextField()
    Gender = models.CharField(max_length=10, choices=GENDER)
    Dob = models.DateField()

    def __str__(self):
        return self.user.username

class EventDetails(models.Model):
    EventType = models.CharField(max_length=50, choices=EVENT)
    NumberOfDays = models.IntegerField()
    GuestCount = models.IntegerField()
    Price = models.IntegerField()
    Description = models.TextField()

    def __str__(self):
        return self.EventType


class StaffDetails(models.Model):
    Name=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    Email=models.EmailField()
    Address=models.TextField()
    Gender=models.CharField(max_length=10, choices=GENDER)
    Dob=models.DateField()
    salary=models.IntegerField()
    experience=models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])

class Booking(models.Model):
    Cust=models.ForeignKey(User,on_delete=models.CASCADE)
    BookingDate=models.DateField(blank=True)
    Menu=models.CharField(max_length=50)
    Details=models.TextField()
    Status=models.CharField(max_length=10,default="pending")
    Eve=models.ForeignKey(EventDetails,on_delete=models.CASCADE)

class FeedbackDetails(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Message=models.TextField()
    Status=models.CharField(max_length=10,default="pending")

    