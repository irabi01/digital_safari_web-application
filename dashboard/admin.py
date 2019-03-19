from django.contrib import admin
from .models import BusRegistartion, BusAndRoutes, CompanyStaff, CompanyInformation
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'phone_number', 'staff_status']
admin.site.register(BusRegistartion)
admin.site.register(BusAndRoutes)
admin.site.register(CompanyStaff, UserProfileAdmin)
admin.site.register(CompanyInformation)
admin.site.site_header = 'Digital Safari Administartion Panel'
