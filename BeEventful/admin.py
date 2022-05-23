from django.contrib import admin
from .models import Booking, EventDetails, FeedbackDetails, UserProfile, StaffDetails

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(EventDetails)
admin.site.register(StaffDetails)
admin.site.register(Booking)
admin.site.register(FeedbackDetails)
