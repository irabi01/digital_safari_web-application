from django.contrib import admin
from .models import Passenger, PaymentInfo

# Register your models here.
admin.site.register(Passenger)
admin.site.register(PaymentInfo)
