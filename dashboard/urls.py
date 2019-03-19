from django.conf.urls import url
from . import views as page

# app_name = 'dashboard'
urlpatterns = [
   # /dashboard/
    url(r'^$', page.home, name ='home_dashboard'),
    url(r'^home/', page.home, name ='home_dashboard'),
    url(r'^new_customer/', page.new_customer, name='new_customer_dashboard'),
    url(r'^routes/', page.route_dashboard, name='route_dashboard'),
    url(r'^bus/(?P<id>\d+)/seat_layout_and_passenger_details/', page.seat_layout_dashboard, name='seat_layout_dashboard'),
    url(r'^new_staff/', page.new_staff, name='new_staff_dashboard'),
    url(r'^new_company/', page.new_company, name='new_company_dashboard'),
    url(r'^profile/', page.profile, name='profile_dashboard'),
    url(r'^all_reports/', page.setting, name='report_dashboard'),
    url(r'^user/auth/login/', page.login_user, name='login_user_dashboard'),
    url(r'^add_bus_and_route/', page.add_bus, name='add_bus_dashboard'),
    url(r'^company_list/', page.company_list, name='company_list'),
    url(r'^registered_bus_list/', page.view_bus, name='view_bus_dashboard'),
    url(r'^added_bus_and_route_list/', page.view_added_bus, name='view_added_bus_dashboard'),
    url(r'^register_new_bus/', page.register_bus, name='register_bus_dashboard'),
    url(r'^customer_List/', page.view_customer, name='view_customer_dashboard'),
    url(r'^list_of_passenger/code_number/(?P<id>\d+)/all/', page.view_all_customer, name='view_all_customer'),
    url(r'^staffs_list/', page.staffs_list, name='staffs_list_dashboard'),
    url(r'^bus/(?P<id>\d+)/delete/$', page.delete_bus, name='delete_bus_dashboard'),
    url(r'^bus/(?P<id>\d+)/update/', page.update_bus, name='update_reg_bus_dashboard'),
    url(r'^staff/(?P<id>\d+)/delete/$', page.delete_staff, name='delete_staff_dashboard'),
    url(r'^bus_and_route/(?P<id>\d+)/delete/', page.delete_bus_route, name='delete_bus_route'),
    url(r'^bus_and_route/(?P<id>\d+)/update/', page.update_bus_route, name='update_bus_route'),
    url(r'^bus_and_route/(?P<id>\d+)/details/', page.view_bus_route, name='view_bus_route'),
    url(r'^passenger_ticket/(?P<id>\d+)/cancel/', page._cancel_ticket, name='_cancel_ticket'),
    url(r'^payment_details/(?P<id>\d+)/delete/', page._delete_all_customer, name='_delete_all_customer'),
]
