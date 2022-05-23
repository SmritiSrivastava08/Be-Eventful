from tkinter import EventType
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

#from django.contrib.auth.decorators import 
from django.contrib import messages
from django.contrib.auth.models import User,auth

from BeEventful.helpers import success_mail,reject_mail
from .forms import BookingForm, ExtendedUserCreationForm, FeedbackForm, ProfileForm, EventForm, StaffForm
from .models import Booking, EventDetails, FeedbackDetails, StaffDetails
from django.contrib.auth.decorators import login_required

# Create your views here.

#Common
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')   

def services(request):
    return render(request,'services.html') 

def logout(request):
    auth.logout(request)
    return redirect('home')

# For User 

def registration(request):
    if request.method=='POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user=form.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()
            return redirect('login')
    else:
        form=ExtendedUserCreationForm()
        profile_form=ProfileForm()

    context={'form':form, 'profile_form':profile_form}
    return render(request,'registration.html',context)

def registration_new(request):
    return render(request,'registration_new.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request,'After_login.html',{'username':username})
        else:
            messages.info(request,'invalid credentials please try again')
            return redirect('login')
    else:
        return render(request,'login.html')

@login_required(login_url="login")
def After_login(request):
    return render(request,'After_login.html')

@login_required(login_url="login")
def wedding_event(request):
    context = {'event_list':EventDetails.objects.filter(EventType='Wedding')}
    return render(request,'wedding_event.html',context)

@login_required(login_url="login")
def birthday_event(request):
    context = {'event_list':EventDetails.objects.filter(EventType='Birthday')}
    return render(request,'birthday_event.html',context)

@login_required(login_url="login")
def corporate_event(request):
    context = {'event_list':EventDetails.objects.filter(EventType='Corporate')}
    return render(request,'corporate_event.html',context)

@login_required(login_url="login")
def social_event(request):
    context = {'event_list':EventDetails.objects.filter(EventType='Social Gathering')}
    return render(request,'social_event.html',context)


# For Admin

def Admin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser==True:
                auth.login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return render(request,'AdminPage.html',{'username':username})
            else:
                messages.info(request,'invalid credentials please try again')
                return redirect('Admin_login')
        else:
            messages.info(request,'invalid credentials please try again')
            return redirect('Admin_login')
    else:
        return render(request,'Admin_login.html')

@login_required(login_url="Admin_login")
def AdminPage(request):
    return render(request,'AdminPage.html')

@login_required(login_url="Admin_login")
def event_list(request):
    context = {'event_list':EventDetails.objects.all()}
    return render(request,'event_list.html',context)

@login_required(login_url="Admin_login")
def event_form(request,id=0):
    if request.method=="GET":
        if id==0:
            event_form = EventForm()
        else:
            event=EventDetails.objects.get(pk=id)
            event_form = EventForm(instance=event)
        return render(request,'event_form.html',{'form':event_form})
    else:
        if id==0:
            event_form = EventForm(request.POST)
        else:
            event=EventDetails.objects.get(pk=id)
            event_form = EventForm(request.POST,instance=event)
        if event_form.is_valid():
            event_form.save()
        return redirect('event_list')

def event_delete(request,id):
    event=EventDetails.objects.get(pk=id)
    event.delete()
    return redirect('event_list')

@login_required(login_url="Admin_login")
def staff_list(request):
    context = {'staff_list':StaffDetails.objects.all()}
    return render(request,'staff_list.html',context)

@login_required(login_url="Admin_login")
def staff_form(request,id=0):
    if request.method=="GET":
        if id==0:
            staff_form = StaffForm()
        else:
            staff=StaffDetails.objects.get(pk=id)
            staff_form = StaffForm(instance=staff)
        return render(request,'staff_form.html',{'form':staff_form})
    else:
        if id==0:
            staff_form = StaffForm(request.POST)
        else:
            staff=StaffDetails.objects.get(pk=id)
            staff_form = StaffForm(request.POST,instance=staff)
        if staff_form.is_valid():
            staff_form.save()
        return redirect('staff_list')

def staff_delete(request,id):
    staff=StaffDetails.objects.get(pk=id)
    staff.delete()
    return redirect('staff_list')

def wedding_booking(request):
    return render(request,'wedding_booking.html')

def booking_form(request,id):
    if request.method=="GET":
        booking_form = BookingForm()

        context={'form':booking_form}
        return render(request,'booking_form.html',context)
    else:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            event=EventDetails.objects.get(pk=id)
            booking=booking_form.save(commit=False)
            booking.Eve=event
            booking.Cust=request.user
            booking.save()
            messages.info(request,'Thank you for booking the event. Please wait till your booking gets approved. You will be notified through your E-mail address')
            return redirect('wedding_event')
        else:
            messages.info(request,'Sorry! Event for this date has already been booked. Please look for another date. Also check you are providing correct date.')
            return redirect('wedding_event')
        

def booking_list(request):
    context = {'booking_list':Booking.objects.filter(Status='pending')}
    return render(request,'booking_list.html',context)

def ApprovedBooking_list(request):
    context = {'ApprovedBooking_list':Booking.objects.filter(Status='Approved')}
    return render(request,'ApprovedBooking_list.html',context)

def booking_delete(request,id):
    booking=Booking.objects.get(pk=id)
    booking.delete()
    return redirect('ApprovedBooking_list')

def booking_status(request,id):
    booking=Booking.objects.get(pk=id)
    booking.Status='Approved'
    user_obj=User.objects.get(username=booking.Cust)
    event=EventDetails.objects.get(EventType=booking.Eve)
    success_mail(user_obj.email,event.EventType,booking.BookingDate,event.Price)
    booking.save()
    messages.info(request,'Successfully Approved')
    return redirect('booking_list')

def booking_reject(request,id):
    booking=Booking.objects.get(pk=id)
    booking.delete()
    user_obj=User.objects.get(username=booking.Cust)
    event=EventDetails.objects.get(EventType=booking.Eve)
    reject_mail(user_obj.email,event.EventType,booking.BookingDate,event.Price)
    messages.info(request,'Successfully Rejected')
    return redirect('booking_list')

#Feedback form and List
def feedback_form(request,id=0):
    if request.method=="GET":
        if id==0:
           feedback_form = FeedbackForm()
        else:
            feedback=FeedbackDetails.objects.get(pk=id)
            feedback_form = FeedbackForm(instance=feedback)
        return render(request,'feedback_form.html',{'form':feedback_form})
    else:
        if id==0:
            feedback_form = FeedbackForm(request.POST)
        else:
            feedback=FeedbackDetails.objects.get(pk=id)
            feedback_form = FeedbackForm(request.POST,instance=feedback)
        if feedback_form.is_valid():
            feedback_form.save()
        return redirect('home')

def feedback_delete(request,id):
    feed=FeedbackDetails.objects.get(pk=id)
    feed.delete()
    return redirect('feedback_list')

@login_required(login_url="Admin_login")
def feedback_list(request):
    context = {'feedback_list':FeedbackDetails.objects.filter(Status='pending')}
    return render(request,'feedback_list.html',context)

def ApprovedFeedback_list(request):
    context = {'ApprovedFeedback_list':FeedbackDetails.objects.filter(Status='Approved')}
    return render(request,'ApprovedFeedback_list.html',context)

def feedback_status(request,id):
    feedback=FeedbackDetails.objects.get(pk=id)
    feedback.Status='Approved'
    feedback.save()
    return redirect('feedback_list')

def accept_feedback(request):
    context = {'accept_feedback':FeedbackDetails.objects.filter(Status='Approved')}
    return render(request,'accept_feedback.html',context)