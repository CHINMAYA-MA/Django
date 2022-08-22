from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [ 
    path("",views.loginUser, name='login'),
    path("about",views.about, name='about'),
    path("forget",views.forget, name='forget'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("shows",views.shows, name='shows'),
    path('signup/', views.signup, name='signup'),
    
]


