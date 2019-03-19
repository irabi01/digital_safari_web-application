from django import forms
from django.contrib.auth.models import User
from .models import BusRegistartion, BusAndRoutes, CompanyStaff, CompanyInformation
from django.contrib.auth.forms import UserCreationForm

class BusRegister(forms.ModelForm):
    class Meta:
        model = BusRegistartion
        fields = ['plate_Number','seat_Number','bus_Type','bus_class','company_name']
        widgets = {
            'plate_Number': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Plate Number'}),
            'seat_Number': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Total Number of Seats'}),
            'company_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Company Name'}),
        }

class CompanyStaffAdd(forms.ModelForm):
    class Meta:
        model = CompanyStaff
        fields = ['phone_number','staff_status','company_name', 'user']
        widgets = {
            'phone_number': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Mobile Number'}),
            # 'email_address': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'E-mail Address'}),
            # 'staff_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Staff Name'}),
            'company_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Company name'}),
        }

class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

class CompanyInformationAdd(forms.ModelForm):
    class Meta:
        model = CompanyInformation
        fields = ['company_name','tiny_number','email_address','business_license','phone_number']
        widgets = {
            'company_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Company Name'}),
            'tiny_number': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Tiny Number'}),
            'email_address': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'E-mail Address'}),
            'business_license': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Business License'}),
            # 'staff_status': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Staff Status'}),
            'phone_number': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Mobile Number'}),
        }

class BusAndRoutesAdd(forms.ModelForm):
    class Meta:
        model = BusAndRoutes
        fields =['plate_Number','from_point','to_point','departure_date','time_of_travel', 'company_name', 'arrival_Time','driver_name','assistant_name','amenity1','amenity2','amenity3','amenity4','dail_fare']
        widgets = {
            # 'plate_Number': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Plate Number'}),
            'departure_date': forms.TextInput(attrs = {'class':'form-control', 'id':'departure', 'placeholder':'Departure date'}),
            'company_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Company Name'}),
            'driver_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Driver Name'}),
            'assistant_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Assistant Name'}),
            'dail_fare': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Fare'}),
        }
