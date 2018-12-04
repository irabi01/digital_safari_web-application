from django.conf.urls import url
from . import views as page

urlpatterns = [
    # url(r'^$', page.login, name ='login_user'),
    url(r'^user/auth/login/', page.login_user, name='login_user_authentication'),
    url(r'^register/', page.register, name='register'),
    url(r'^company_login/', page.company_login, name='company_login'),
    url(r'^logout/', page.logout_user, name = 'logout_user'),
    url(r'^user/auth/register/staff/', page.get_registration, name = 'get_registration')
]
