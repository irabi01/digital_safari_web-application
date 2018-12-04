from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import BusAndRoutes, BusRegistartion
from datetime import datetime


# Create your views here.
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

def availableRoutes(request):
    print("welcome to the available bus")
    startingpoint = request.POST.get('startingpoint')
    endpoint = request.POST.get('endpoint')
    departuredate = request.POST.get('departuredate')
    # x = startingpoint[0:3]
    print(startingpoint)
    # print(x)
    print(endpoint)
    print(departuredate)
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint , to_point__icontains = endpoint , departure_date__icontains = departuredate).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint , to_point__icontains = endpoint , departure_date__icontains = departuredate)
    myDate = datetime.now()
    context = {
        # 'x_variable': x,
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
        # return redirect('/digital_safari/availableRoutes/')
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

def payment_option(request, id = None):
    myDate = datetime.now()
    get_bus_details_to_payment_page = get_object_or_404(BusAndRoutes, id = id)
    context = {
        'date': myDate,
        'full_details_to_payment_page':get_bus_details_to_payment_page,
    }
    return render(request, 'digital_safari/payment_option.html',context)



# Edit this function future on in order to work correctly ...... By 01Coder from soft-Touch
def search(request):
    if request.method == "POST":
        startingpoint_variable = request.POST['spoint']
        endpoint_variable = request.POST['fpoint']
        departuredate_variable = request.POST['departure']
    else:
        startingpoint_variable = ""
        endpoint_variable = ""
        departuredate_variable = ""
    filtered_Routes = BusAndRoutes.objects.filter(from_point = startingpoint_variable)
    context = {
        'filtered_Routes':filtered_Routes
    }
    return render(request, 'digital_safari/available_bus.html', context)

def twelvethousand(request):
    print("welcome to the available bus")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    get_routes = BusAndRoutes.objects.filter( dail_fare = '22000').count()
    countRoutes = BusAndRoutes.objects.filter( dail_fare = '22000')
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

#************************* filter by bus Class (Luxury or Semi-Luxury)***********
def search_luxury(request):
    print("search Luxury bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, bus_class = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, bus_class = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

def search_semi_luxury(request):
    print("search semi Luxury bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, bus_class = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, bus_class = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

def search_ordinary_bus(request):
    print("search search_ordinary_bus bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, bus_class = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, bus_class = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)



#custom page not found ..... by 01Coder from soft-touch technology
def error404(request, exception):
    # context = {
    #     'date': myDate,
    # }
    return render(request, 'digital_safari/error_404.html', {})


#*************************** filter by departure time **********************
def _0600am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    #startingpoint = startingpoint.lower()#solve this error (lower)
    #endpoint = endpoint.lower()#solve this error (lower)
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

def _0630am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _0700am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _0730am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _0800am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _0830am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _0900am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _0930am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)
def _1000am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1030am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1100am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1130am(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

def _1200pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1230pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1300pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1330pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1400pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1430pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1500pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1530pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1600pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1630pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1700pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1730pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1800pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1830pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1900pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _1930pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)


def _2000pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)

def _2030pm(request):
    print("search saa 1200 asubuhi bus for respective routes")
    startingpoint = request.POST.get('startingpoint')#from
    endpoint = request.POST.get('endpoint')#to
    departuredate = request.POST.get('departuredate')
    filter_field = request.POST.get('for_searching_data')
    get_routes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field).count()
    countRoutes = BusAndRoutes.objects.filter(from_point__icontains = startingpoint, to_point__icontains = endpoint, departure_date__icontains = departuredate, time_of_travel = filter_field)
    myDate = datetime.now()
    context = {
        'date': myDate,
        'countRoutes':countRoutes,
        'get_routes':get_routes,
        'startingpoint':startingpoint,
        'endpoint':endpoint,
        'departuredate':departuredate
    }
    if get_routes > 0:
        return render(request, 'digital_safari/available_bus.html', context)
    else:
        return render(request, 'digital_safari/route_error_page.html', context)
