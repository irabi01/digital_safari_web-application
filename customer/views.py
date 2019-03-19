from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import BusAndRoutes, BusRegistartion
from datetime import datetime
from django.db.models import Q
from .models import Passenger, PaymentInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.template.loader import get_template
from .render import Render

# Create your views here.
def generate_single_view(request, id):
    pass_details = PaymentInfo.objects.get(id = id)
    _pay = pass_details.secrete_code
    print(_pay)
    get_passenger_details = Passenger.objects.filter(secretecode = _pay)
    today = timezone.now()
    params = {
        'today': today,
        'datas': get_passenger_details,
        'request': request,
        'passenger': pass_details,
    }
    return Render.render('digital_safari/pdf.html', params)

def home(request):
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, 'digital_safari/home.html',context)

def about(request):
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, 'digital_safari/about.html', context)

def contact(request):
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, 'digital_safari/contact.html', context)

def login_user(request):
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, 'authentication/login.html', context)

def get_current_time(request):
    myDate = datetime.now()
    context = {
        'date': myDate
    }
    return render(request, 'digital_safari/footer.html', context)

def searched_routes(request):
    fr_p = request.GET.get('startingpoint', None)
    to_p = request.GET.get('endpoint', None)
    dep = request.GET.get('departuredate', None)
    # ret = request.GET.get('return', None)
    query = request.GET.get('q', None)
    myDate = datetime.now()
    route = BusAndRoutes.objects.all()
    count_route = BusAndRoutes.objects.filter(from_point = fr_p, to_point = to_p, departure_date = dep).count()
    if query is not None:
        route = route.filter(
            Q(from_point__icontains = query) |
            Q(to_point__icontains = query) |
            Q(departure_date__icontains = query) |
            Q(bus_class__icontains = query) |
            Q(dail_fare__icontains = query) |
            Q(company_Name__icontains = query)
        )
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
    }
    if count_route > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

def seatlayout(request, id = None):
    myDate = datetime.now()
    get_bus_details = get_object_or_404(BusAndRoutes , id = id)
    context = {
        'date': myDate,
        'seat_layout_details': get_bus_details,
    }
    return render(request, 'digital_safari/seat_layout.html', context)

def passengers_details(request):
    print("passengers details are going to be submitted")
    if request.method == "POST":
        # for passenger details
        seatnumber = request.POST.getlist('seatnumber')
        nauli = request.POST.getlist('nauli')
        firstname = request.POST.getlist('firstname')
        lastname = request.POST.getlist('lastname')
        boardingpoint = request.POST.getlist('boardingpoint')
        dropingpoint = request.POST.getlist('dropingpoint')
        secretecode = request.POST.getlist('secretecode')
        ticket_number = request.POST.getlist('ticket_number')
        # for payment details
        total_amount = request.POST.get('amount_total')
        phonenumber = request.POST.get('phonenumber')
        emailaddress = request.POST.get('emailaddress')
        payment_status = request.POST.get('paymentstatus')
        refence_number = request.POST.get('referencenumber')
        secrete_code = request.POST.get('secrete_code')
        totalseats = request.POST.get('totalseats')
        from_p = request.POST.get('from_point_orign')
        to_d = request.POST.get('to_point_destination')
        date_of_t = request.POST.get('dateoftravel')
        time_of_t = request.POST.get('timeoftravel')
        plate_n = request.POST.get('platenumber')
        operator = request.POST.get('operator')
        arrivaltime = request.POST.get('arrivaltime')
        bustype = request.POST.get('bustype')
        busclass = request.POST.get('busclass')
        for fn, ln, bp, dp, sn, nauli, sc, tn in zip(firstname, lastname, boardingpoint, dropingpoint, seatnumber, nauli, secretecode, ticket_number):
            print(fn)
            print(ln)
            print(bp)
            print(dp)
            print(sn)
            print(nauli)
            print(sc)
            print(tn)
            passenger_object = Passenger(first_name = fn, last_name = ln, boarding_point = bp, droping_point = dp, seatnumber = sn, nauli = nauli, secretecode = sc, ticket_number = tn)
            passenger_object.save()
        print('********************* payment details *********************')
        print(total_amount)
        print(emailaddress)
        print(phonenumber)
        print(payment_status)
        print(refence_number)
        print(secrete_code)
        print(totalseats)
        print(from_p)
        print(to_d)
        print(date_of_t)
        print(time_of_t)
        print(plate_n)
        print(operator)
        print(arrivaltime)
        print(bustype)
        print(busclass)
        payment_object = PaymentInfo(secrete_code = secrete_code, payment_status = payment_status, refence_number = refence_number, phonenumber = phonenumber, emailaddress = emailaddress, totalseats = totalseats, amount_total = total_amount, from_p = from_p, to_d = to_d, date_of_t = date_of_t, time_of_t = time_of_t, plate_n = plate_n, operator = operator, arrivaltime = arrivaltime, bustype = bustype, busclass = busclass)
        payment_object.save()
        return redirect('/passengers_details/payment_option/')
        # return redirect('payment_option')
    else:
        return redirect('homepage')

def payment_option(request):
    myDate = datetime.now()
    # get_bus_details = get_object_or_404(BusAndRoutes, id = id)
    get_payment_info = PaymentInfo.objects.latest('id')
    _data = get_payment_info.secrete_code
    print(_data)
    get_passenger_details = Passenger.objects.filter(secretecode = _data)
    context = {
        'date': myDate,
        'full_details_to_payment_page':get_passenger_details,
        'bus_details_payment_page':get_payment_info,
    }
    return render(request, 'digital_safari/payment_option.html', context)


#custom page not found ..... by 01Coder from soft-touch technology
def error404(request, exception):
    return render(request, 'digital_safari/error_404.html', {})

def error500(request):
    return render(request, 'digital_safari/error_500.html', {})


#*************************** filter by departure time **********************
