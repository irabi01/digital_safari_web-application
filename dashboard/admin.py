from django.contrib import admin
from .models import BusRegistartion, BusAndRoutes, CompanyStaff, CompanyInformation
# Register your models here.
admin.site.register(BusRegistartion)
admin.site.register(BusAndRoutes)
admin.site.register(CompanyStaff)
admin.site.register(CompanyInformation)
