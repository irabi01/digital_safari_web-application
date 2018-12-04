from django.shortcuts import render, get_object_or_404, redirect
from .forms import BusRegister, BusAndRoutesAdd, CompanyStaffAdd, CompanyInformationAdd
from django.contrib import messages
from .models import BusRegistartion, BusAndRoutes, CompanyStaff, CompanyInformation
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def new_customer(request):
    return render(request, 'dashboard/add_customer.html')

def login_user(request):
    return render(request, 'authentication/login.html')

def new_staff(request):
    form = CompanyStaffAdd(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Staff Is Added Successfully')
        return redirect('/dashboard/staffs_list/')
    context = {
        'form':form
    }
    return render(request, 'dashboard/add_staff.html', context)

def new_company(request):
    form = CompanyInformationAdd(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Company Registered Successfully')
        return redirect('/dashboard/company_list/')
    context = {
        'form':form
    }
    return render(request, 'dashboard/register_company.html', context)

def profile(request):
    return render(request, 'dashboard/profile.html')

def setting(request):
    return render(request, 'dashboard/setting.html')

def company_list(request):
    company_list = CompanyInformation.objects.all()
    context = {
        'company_list':company_list
    }
    return render(request, 'dashboard/company_list.html', context)

def staffs_list(request):
    count_staffs = CompanyStaff.objects.all().count()
    staffs = CompanyStaff.objects.all()
    context = {
        'staffs':staffs,
        'count_staffs':count_staffs
    }
    return render(request, 'dashboard/staff_list.html', context)

def view_customer(request):
    return render(request, 'dashboard/view_customer.html')

def register_bus(request):
    busR = BusRegister(request.POST or None)
    if busR.is_valid():
        busR.save()
        messages.success(request, 'New Bus Is Added Successfully')
        return redirect('/dashboard/registered_bus_list/')
    context = {
        'busR': busR,
    }
    return render(request, 'dashboard/register_bus.html', context)

def add_bus(request):
    busandroute = BusAndRoutesAdd(request.POST or None)
    if busandroute.is_valid():
        busandroute.save()
        messages.success(request, 'New Route Is Added Successfully')
        return redirect('/dashboard/added_bus_and_route_list/')
    context = {
        'busandroute': busandroute
    }
    return render(request, 'dashboard/add_bus.html', context)

def view_bus(request):
    getbusinfo = BusRegistartion.objects.all()
    context = {
        'bus_detail': getbusinfo,
    }
    return render(request, 'dashboard/view_bus.html', context)

def view_added_bus(request):
    get_route_info = BusAndRoutes.objects.all()
    context = {
        'route_info':get_route_info
    }
    return render(request, 'dashboard/view_added_bus_and_route.html', context)

def bus_registration(request):
    busR = BusRegister(request.POST or None)
    if busR.is_valid():
        instance = busR.save(commit = False )
        instance.save()
        messages.success(request, 'Bus registered successfully')
    context = {
        'busR': busR,
    }
    return render(request, 'dashboard/register_bus.html',context)

def delete_bus(request, id):
    bus_id_registration = get_object_or_404(BusRegistartion , id = id)
    bus_id_registration.delete()
    messages.success(request, 'Bus Has Been Deleted successfully')
    return redirect('/dashboard/registered_bus_list/')

def update_bus(request, id):
    update_reg_bus = get_object_or_404(BusRegistartion , id = id)
    busR = BusRegister(request.POST or None, instance = update_reg_bus)
    if busR.is_valid():
        busR.save()
        messages.success(request, 'Bus is Updated Successfully')
        return redirect('/dashboard/registered_bus_list/')
    context = {
        'busR': busR,
    }
    return render(request, 'dashboard/register_bus.html', context)

def delete_staff(request, id):
    get_staff_id = get_object_or_404(CompanyStaff , id = id)
    get_staff_id.delete()
    messages.success(request, 'Staff Has Been Deleted successfully')
    return redirect('/dashboard/staffs_list/')
