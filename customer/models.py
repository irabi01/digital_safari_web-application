from django.db import models

# Create your models here.
class Passenger(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    boarding_point = models.CharField(max_length = 50)
    droping_point = models.CharField(max_length = 50)
    seatnumber = models.CharField(max_length = 50)
    nauli = models.CharField(max_length = 50)
    secretecode = models.CharField(max_length = 20)
    ticket_number = models.CharField(max_length = 20)
    class Meta:
        verbose_name_plural = "passengers details"
    def __str__(self):
        return 'seat number '+ self.seatnumber

class PaymentInfo(models.Model):
    payment_status = models.CharField(max_length = 50)
    refence_number = models.CharField(max_length = 100)
    phonenumber = models.CharField(max_length = 50)
    emailaddress = models.EmailField(max_length = 100)
    secrete_code = models.CharField(max_length = 100)
    totalseats = models.CharField(max_length = 3)
    amount_total = models.IntegerField()
    from_p = models.CharField(max_length = 50)
    to_d = models.CharField(max_length = 50)
    date_of_t = models.CharField(max_length = 30)
    time_of_t = models.CharField(max_length = 20)
    plate_n = models.CharField(max_length = 20)
    operator = models.CharField(max_length = 50)
    arrivaltime = models.CharField(max_length = 20)
    bustype = models.CharField(max_length = 20)
    busclass = models.CharField(max_length = 20)
    class Meta:
        verbose_name_plural = "payment information"
    def __str__(self):
        return self.emailaddress
