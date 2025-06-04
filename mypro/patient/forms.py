from typing import Any,Mapping
from django.core.files.base import File 
from django.db.models.base import Model 
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import patient

class QuickPatientForm(ModelForm):
    class Meta:
        model=patient
        fields=['name','age','gender','detail','medicine_detail','amount','next_visit']

    def __init__(self,*args,**kwargs):
       super(QuickPatientForm, self).__init__(*args, **kwargs)
       for field in self.fields:
        self.fields[field].widget.attrs['class']='form-control'