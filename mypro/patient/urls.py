from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('doctor/login',views.doctor_login,name='doctor_login'),
    path('doctor/logout',views.doctor_logout,name='doctor_logout'),
     path('doctor/reset-password',views.doctor_reset_password,name='doctor_reset_password'),
]

