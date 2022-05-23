from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='serivces'),
    path('registration',views.registration,name='registration'),
    path('registration_new',views.registration_new,name='registration_new'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('Admin_login',views.Admin_login,name='Admin_login'),
    path('AdminPage',views.AdminPage,name='AdminPage'),
    path('After_login',views.After_login,name='After_login'),

    path('event_list',views.event_list,name='event_list'),
    path('event_form',views.event_form,name='event_form'),
    path('event_form/<int:id>/',views.event_form,name='event_update'),
    path('event_delete/<int:id>/',views.event_delete,name='event_delete'),

    path('wedding_event',views.wedding_event,name='wedding_event'),
    path('birthday_event',views.birthday_event,name='birthday_event'),
    path('corporate_event',views.corporate_event,name='corporate_event'),
    path('social_event',views.social_event,name='social_event'),

    path('staff_list',views.staff_list,name='staff_list'),
    path('staff_form',views.staff_form,name='staff_form'),
    path('staff_form/<int:id>/',views.staff_form,name='staff_update'),
    path('staff_delete/<int:id>/',views.staff_delete,name='staff_delete'),

    path('booking_form/<int:id>/',views.booking_form,name='booking_form'),
    path('booking_list',views.booking_list,name='booking_list'),
    path('ApprovedBooking_list',views.ApprovedBooking_list,name='ApprovedBooking_list'),
    path('booking_delete/<int:id>/',views.booking_delete,name='booking_delete'),
    path('booking_status/<int:id>/',views.booking_status,name='booking_status'),
    path('booking_reject/<int:id>/',views.booking_reject,name='booking_reject'),

    path('feedback_list',views.feedback_list,name='feedback_list'),
    path('feedback_form',views.feedback_form,name='feedback_form'),
    path('feedback_delete/<int:id>/',views.feedback_delete,name='feedback_delete'),
    path('accept_feedback',views.accept_feedback,name='accept_feedback'),
    path('feedback_status/<int:id>/',views.feedback_status,name='feedback_status'),
    path('ApprovedFeedback_list',views.ApprovedFeedback_list,name='ApprovedFeedback_list'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]