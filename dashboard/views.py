from django.shortcuts import render, get_object_or_404, redirect
from .forms import BusRegister, BusAndRoutesAdd, CompanyStaffAdd, CompanyInformationAdd
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from .models import BusRegistartion, BusAndRoutes, CompanyStaff, CompanyInformation
from customer.models import Passenger, PaymentInfo
from django.contrib.auth.models import User
from django.template.loader import get_template
from .render import Render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def home(request):
    p = get_object_or_404(User, id = request.user.id)
    get_user = p.user.company_name
    status = p.user.staff_status
    print(status)
    print(get_user)
    pay = PaymentInfo.objects.filter(operator = get_user).count()
    print(pay)
    count_staffs = CompanyStaff.objects.filter(company_name = get_user).count()
    # p_info = Passenger.objects.filter(secretecode = pay.secrete_code).count() hapa bado
    b_info = BusRegistartion.objects.filter(company_name = get_user).count()
    context = {
        'p_info':pay,
        'b_info':b_info,
        'c_info':count_staffs,
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/home.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def new_customer(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    print(status)
    context = {
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/add_customer.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def route_dashboard(request):
    p = get_object_or_404(User, id = request.user.id)
    get_user = p.user.company_name
    print(get_user)
    status = p.user.staff_status
    print(status)
    fr_p = request.GET.get('startingpoint', None)
    to_p = request.GET.get('endpoint', None)
    dep = request.GET.get('departuredate', None)
    # ret = request.GET.get('return', None)
    myDate = datetime.now()
    route = BusAndRoutes.objects.filter(company_name = get_user)
    count_route = BusAndRoutes.objects.filter(company_name = get_user, from_point = fr_p, to_point = to_p, departure_date = dep).count()
    if fr_p is not None:
        route = route.filter(from_point__icontains = fr_p)
    if to_p is not None:
        route = route.filter(to_point__icontains = to_p)
    if dep is not None:
        route = route.filter(departure_date__icontains = dep)
    # if ret is not None:
    #     route = route.filter(from_point__icontains = ret)
    context = {
        'date': myDate,
        'route':route,
        'count_route':count_route,
        'fr_point': fr_p,
        'to_dest': to_p,
        'depart': dep,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/routes.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def seat_layout_dashboard(request, id = None):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    print(status)
    myDate = datetime.now()
    get_bus_details = get_object_or_404(BusAndRoutes , id = id)
    context = {
        'date': myDate,
        'bus_details': get_bus_details,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/seat_layout.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    return render(request, 'authentication/login.html')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def new_staff(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    form = CompanyStaffAdd(request.POST or None)
    if form.is_valid():
        form.save()
        CompanyStaff.objects.create(user = user)
        messages.success(request, 'New Staff Is Added Successfully')
        return redirect('/dashboard/staffs_list/')
    context = {
        'form':form,
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/add_staff.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def new_company(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    form = CompanyInformationAdd(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Company Registered Successfully')
        return redirect('/dashboard/company_list/')
    context = {
        'form':form,
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/register_company.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def profile(request):
    p = get_object_or_404(User, id = request.user.id)
    profile = CompanyStaff.objects.filter(user = p)
    status = p.user.staff_status
    print(status)
    print('******************* user ********************')
    print(profile)
    print('******************* user ********************')
    context = {
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/profile.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def setting(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    print(status)
    context = {
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/reports.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def company_list(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    print(status)
    company_list = CompanyInformation.objects.all()
    context = {
        'company_list':company_list,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/company_list.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def staffs_list(request):
    p = get_object_or_404(User, id = request.user.id)
    get_user = p.user.company_name
    status = p.user.staff_status
    print(status)
    count_staffs = CompanyStaff.objects.filter(company_name = get_user).count()
    staffs = CompanyStaff.objects.filter(company_name = get_user)
    context = {
        'staffs':staffs,
        'count_staffs':count_staffs,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/staff_list.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def view_customer(request):
    query = request.GET.get('secrete_code', None)
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    get_user = p.user.company_name
    print(status)
    print(get_user)
    pay_info = PaymentInfo.objects.filter(operator = get_user)
    pay_info_number = PaymentInfo.objects.filter(operator = get_user).count()
    if query is not None:
        pay_info = pay_info.filter(secrete_code = query)
    context = {
        'pay_info':pay_info,
        'pay_info_number':pay_info_number,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/view_customer.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def view_all_customer(request, id):
    p = get_object_or_404(User, id = request.user.id)
    query = request.GET.get('secrete_code', None)
    status = p.user.staff_status
    print(status)
    pay_info = get_object_or_404(PaymentInfo, id = id)
    passenger_object = Passenger.objects.filter(secretecode = pay_info.secrete_code)
    context = {
        'profile':p,
        'status':status,
        'pay_info':pay_info,
        'passengers':passenger_object,
    }
    return render(request, 'dashboard/customer_single_details.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def register_bus(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    busR = BusRegister(request.POST or None)
    if busR.is_valid():
        busR.save()
        messages.success(request, 'New Bus Is Added Successfully')
        return redirect('/dashboard/registered_bus_list/')
    context = {
        'busR': busR,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/register_bus.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def add_bus(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    busandroute = BusAndRoutesAdd(request.POST or None)
    if busandroute.is_valid():
        busandroute.save()
        messages.success(request, 'New Route Is Added Successfully')
        return redirect('/dashboard/added_bus_and_route_list/')
    context = {
        'busandroute': busandroute,
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/add_bus.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def view_bus(request):
    p = get_object_or_404(User, id = request.user.id)
    get_user = p.user.company_name
    status = p.user.staff_status
    print(status)
    getbusinfo = BusRegistartion.objects.filter(company_name = get_user)
    count_bus = BusRegistartion.objects.filter(company_name = get_user).count()
    print(getbusinfo)
    context = {
        'bus_detail': getbusinfo,
        'count_bus':count_bus,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/view_bus.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def view_added_bus(request):
    p = get_object_or_404(User, id = request.user.id)
    get_user = p.user.company_name
    status = p.user.staff_status
    print(status)
    get_route_info = BusAndRoutes.objects.filter(company_name = get_user)
    count_route_info = BusAndRoutes.objects.filter(company_name = get_user).count()
    context = {
        'route_info':get_route_info,
        'count_route_info':count_route_info,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/view_added_bus_and_route.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def bus_registration(request):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    busR = BusRegister(request.POST or None)
    if busR.is_valid():
        instance = busR.save(commit = False )
        instance.save()
        messages.success(request, 'Bus registered successfully')
    context = {
        'busR': busR,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/register_bus.html',context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def delete_bus(request, id):
    bus_id_registration = get_object_or_404(BusRegistartion , id = id)
    bus_id_registration.delete()
    messages.success(request, 'Bus Has Been Deleted successfully')
    return redirect('/dashboard/registered_bus_list/')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def update_bus(request, id):
    update_reg_bus = get_object_or_404(BusRegistartion , id = id)
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    busR = BusRegister(request.POST or None, instance = update_reg_bus)
    if busR.is_valid():
        instance = busR.save(commit = False)
        instance.save()
        messages.success(request, 'Bus Updated Successfully')
        return redirect('view_bus_dashboard')
    context = {
        'busR': busR,
        'profile':p,
        'status':status
    }
    return render(request, 'dashboard/register_bus.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def delete_staff(request, id):
    get_staff_id = get_object_or_404(CompanyStaff , id = id)
    get_staff_id.delete()
    messages.success(request, 'Staff Has Been Deleted successfully')
    return redirect('/dashboard/staffs_list/')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def _cancel_ticket(request, id):
    get_pass_id = get_object_or_404(Passenger, id = id)
    get_pass_id.delete()
    messages.info(request, 'Ticket Canceled successfully')
    # return HttpResponseRedirect(reverse('view_all_customer'))
    return redirect('/dashboard/customer_List/')#hapa bado kuna kazi ya kudirect message

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def _delete_all_customer(request, id):
    get_pay_id = get_object_or_404(PaymentInfo, id = id)
    get_pay_id.delete()
    messages.info(request, 'Ticket Canceled successfully')
    return redirect('/dashboard/customer_List/')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def delete_bus_route(request, id):
    get_bus_id = get_object_or_404(BusAndRoutes, id = id)
    get_bus_id.delete()
    messages.info(request, 'Route Deleted successfully')
    return redirect('view_added_bus_dashboard')

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def update_bus_route(request, id):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    bus_routes_id = get_object_or_404(BusAndRoutes, id = id)
    busandroute = BusAndRoutesAdd(request.POST or None, instance = bus_routes_id)
    if busandroute.is_valid():
        busandroute.save()
        messages.info(request, 'Route Updated Successfully')
        return redirect('view_added_bus_dashboard')
    context = {
        'busandroute': busandroute,
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/add_bus.html', context)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url = '/dashboard/user/auth/login/')
def view_bus_route(request, id):
    p = get_object_or_404(User, id = request.user.id)
    status = p.user.staff_status
    get_bus_id = get_object_or_404(BusAndRoutes, id = id)
    context = {
        'bus_and_route_detal':get_bus_id,
        'profile':p,
        'status':status,
    }
    return render(request, 'dashboard/bus_and_route_details.html', context)
