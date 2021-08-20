#
# from django import forms
#
# class NameForm(forms.Form):
#     name = forms.CharField(label='name', max_length=100)
#     email = forms.EmailField()

from django import forms
from .models import *


Manufacture=[
    ('Tata','TATA MOTOR'),
    ('Mahindra & Mahindra ltd','Mahindra & Mahindra ltd'),
]
Model=[
    ('BOLERO CAMPER GOLD 2WD','BOLERO CAMPER GOLD 2WD'),
    ('HONDA','HONDA')
]
VType=[
    ('CAMPER','CAMPER'),
    ('SEDAN','SEDAN')
]
Rto=[
    ('BARBIL,ODISHA','BARBIL,ODISHA'),
    ('MAHROULI,DELHI','MAHROULI,DELHI')
]

INTEGER_CHOICES=[tuple([x,x]) for x in range(2000,2014)]

Fuel=[
    ('DIESEL','DIESEL'),
    ('PETROL','PETROL')
]

class Vechicle_Detail(forms.ModelForm):
    class Meta:
        model = Vechicle
        fields = ['SAP_Code','Ledger_Name','Manufacturer','Model','Vehicle_Type','Base_Km','RTO']
        label = ['SAP Code','Ledger Name','Manufacturer','Model','Vehicle type','Base KM','RTO']
        widgets ={
            'SAP_Code':forms.TextInput(attrs={'class':'form-control glyphicon glyphicon-envelope'}),
            'Ledger_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Manufacturer': forms.Select(attrs={'class':'form-control fa fa-home'},choices=Manufacture),
            'Model': forms.Select(attrs={'class':'form-control'},choices=Model),
            'Vehicle_Type': forms.Select(attrs={'class':'form-control'},choices=VType),
            'Base_Km': forms.TextInput(attrs={'class':'form-control'}),
            'RTO': forms.Select(attrs={'class':'form-control'},choices=Rto),
        }


class Engine_Detail(forms.ModelForm):
    class Meta:
        model = Engine
        fields = ['Model_year','Chassis_No','Fuel_TYPE','old_vehicle_No']
        label = ['Model year','Chassis No','Fuel TYPE','old vehicle No']
        widgets = {
            'Model_year': forms.Select(attrs={'class': 'form-control'},choices=INTEGER_CHOICES),
            'Chassis_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Fuel_TYPE': forms.Select(attrs={'class': 'form-control'}, choices=Fuel),
            'old_vehicle_No': forms.TextInput(attrs={'class': 'form-control'}),
        }