from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path( '', views.Index, name="home" ),
    path( 'contact/',views.contact.as_view() , name="contact" ),
    path( 'projects/',views.project , name="projects" ),
    path( 'thankyou/',views.thankyou , name="thankyou" ),
    path( 'about/',views.about , name="about" ),
]
