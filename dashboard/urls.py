from django.conf.urls import url
from . import views as page

# app_name = 'dashboard'
urlpatterns = [
   # /dashboard/
    url(r'^$', page.home, name ='home_dashboard'),
    url(r'^home/', page.home, name ='home_dashboard'),
    url(r'^new_customer/', page.new_customer, name='new_customer_dashboard'),
    url(r'^new_staff/', page.new_staff, name='new_staff_dashboard'),
    url(r'^new_company/', page.new_company, name='new_company_dashboard'),
    url(r'^profile/', page.profile, name='profile_dashboard'),
    url(r'^setting/', page.setting, name='setting_dashboard'),
    url(r'^user/auth/login/', page.login_user, name='login_user_dashboard'),
    url(r'^add_bus_and_route/', page.add_bus, name='add_bus_dashboard'),
    url(r'^company_list/', page.company_list, name='company_list'),
    url(r'^registered_bus_list/', page.view_bus, name='view_bus_dashboard'),
    url(r'^added_bus_and_route_list/', page.view_added_bus, name='view_added_bus_dashboard'),
    url(r'^register_new_bus/', page.register_bus, name='register_bus_dashboard'),
    url(r'^customer_List/', page.view_customer, name='view_customer_dashboard'),
    url(r'^staffs_list/', page.staffs_list, name='staffs_list_dashboard'),
    #url(r'^add_bus_and_routes/', page.add_bus_and_routes, name='add_bus_and_routes_dashboard'),
    url(r'^bus/(?P<id>\d+)/delete/$', page.delete_bus, name='delete_bus_dashboard'),
    url(r'^bus/(?P<id>\d+)/update/$', page.update_bus, name='update_reg_bus_dashboard'),
    url(r'^staff/(?P<id>\d+)/delete/$', page.delete_staff, name='delete_staff_dashboard'),
]
