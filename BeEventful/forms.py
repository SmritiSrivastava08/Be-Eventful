from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking, EventDetails, FeedbackDetails, StaffDetails, UserProfile

class ExtendedUserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def save(self,commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('Phone_No','Address','Gender','Dob')
        labels = {
            'Dob' : 'Date of Birth (Format: MM/DD/YYYY])',
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ('EventType','NumberOfDays','GuestCount','Price','Description')
        labels = {
            'EventType' : 'Type of Event',
            'NumberOfDays' : 'Number of Day for event',
            'GuestCount' : 'Maximum Guest Count',
            'Price' : 'Price (As per maximum guest count)'
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('Name','Phone_No','Email','Address','Gender','Dob','salary','experience')
        labels={
            'Phone_No': 'Phone Number',
            'Dob':'Date of Birth',
            'Experience':'Experience (Number of Years)'
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = ('BookingDate','Menu','Details')
        labels = {
                'BookingDate' : 'Date of Booking (Format: MM/DD/YYYY)',
            }

    def clean_BookingDate(self):
        BookingDate=self.cleaned_data.get('BookingDate')
        for instance in Booking.objects.all():
            if instance.BookingDate == BookingDate:
                raise forms.ValidationError('This date is already booked')
        return BookingDate

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=FeedbackDetails
        fields=('Name','Email','Message')
