from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('doctor/login',views.doctor_login,name='doctors_login'),
]

