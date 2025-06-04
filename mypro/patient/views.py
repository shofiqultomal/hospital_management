from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .forms import QuickPatientForm

# Create your views here.
def home(request):
    return render(request,'home.html')

# doctor login

def doctor_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if user:
           login(request,user)
           return redirect('/')
        else:
            messages.warning(request,"Invalid username or passwoard !")
            return redirect('doctor_login')
            
    return render(request,'login.html',{'page_title':'Doctor login'})


def doctor_logout(request):
    logout(request)
    return redirect('/')


def doctor_reset_password(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if request.method=='POST':
        password=request.POST.get('password')
        request.user.set_password(password)
        messages.success(request, "Password has been changed .")
        return redirect('doctor_login')
    else:
            
        return render(request,'reset_password.html')

# doctor dashboard
def doctor_dashboard(request):
    return render(request,'doctor-dashboard.html')

# doctor quick add patient
def quick_add_patient(request):
    if request.method=='POST':

        form = QuickPatientForm(request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request,"patient added successfully !")
            return redirect('quick_add_patient')
        else:
            messages.warning(request,"samething is went to be waring !")
            return redirect('quick_add_patient')
         
         
    else:
            form = QuickPatientForm

            return render(request,'quick-add-patient-form.html',{'form':form})







