from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# Create your models here.
class CompanyInformation(models.Model):
    company_name = models.CharField(max_length = 100)
    tiny_number = models.CharField(max_length = 100)
    email_address = models.EmailField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    business_license = models.CharField(max_length = 100)
    # staff_status = models.CharField(max_length = 50, default = 'Administrator')
    class Meta:
        verbose_name_plural = "Company Information"
    def __str__(self):
        return self.company_name


class BusRegistartion(models.Model):
    aina_ya_bus = (
        ('Yutong','Yutong'),('Zhong Tong','Zhong Tong'),('Golden Dragon','Golden Dragon')
    )
    aina_ya_class = (
        ('Luxury','Luxury'),('Semi-Luxury','Semi-Luxury'),('Ordinary','Ordinary')
    )
    plate_Number = models.CharField(max_length = 20)
    seat_Number = models.CharField(max_length=5)
    company_name = models.CharField(max_length=50)
    bus_Type = models.CharField(max_length=50, choices = aina_ya_bus)
    bus_class = models.CharField(max_length=50, choices = aina_ya_class)
    class Meta:
        verbose_name_plural = "Bus Registartion"
    def __str__(self):
        return self.plate_Number

class BusAndRoutes(models.Model):
    amenity_one = (
        ('Television','Television'),('None','None')
    )
    amenity_two = (
        ('Wi-fi','Wi-fi'),('None','None')
    )
    amenity_three = (
        ('Charging-service','Charging-service'),('None','None')
    )
    amenity_four = (
        ('Drinks','Drinks'),('None','None')
    )
    form_orign = (
        ('Arusha','Arusha'),('Dar es salaam','Dar es salaam'),('Dodoma','Dodoma'),('Morogoro','Morogoro'),
        ('Bukoba','Bukoba'),('Moshi','Moshi'),('Kilimanjaro','Kilimanjaro'),('Singida','Singida'),('Tabora','Tabora'),
        ('Tanga','Tanga'),('Iringa','Iringa'),('Songea','Songea'),('Mbeya','Mbeya'),('Mtwara','Mtwara'),
        ('Ruvuma','Ruvuma'),('Kigoma','Kigoma'),('Mombasa','Mombasa'),('Mwanza','Mwanza'),('Babati','Babati'),
        ('Sumbawanga','Sumbawanga')
    )
    to_destination = (
        ('Arusha','Arusha'),('Dar es salaam','Dar es salaam'),('Dodoma','Dodoma'),('Morogoro','Morogoro'),
        ('Bukoba','Bukoba'),('Moshi','Moshi'),('Kilimanjaro','Kilimanjaro'),('Singida','Singida'),('Tabora','Tabora'),
        ('Tanga','Tanga'),('Iringa','Iringa'),('Songea','Songea'),('Mbeya','Mbeya'),('Mtwara','Mtwara'),
        ('Ruvuma','Ruvuma'),('Kigoma','Kigoma'),('Mombasa','Mombasa'),('Mwanza','Mwanza'),('Babati','Babati'),
        ('Sumbawanga','Sumbawanga')
    )
    travell_time = (
        ('06:00am','06:00am'),('06:30am','06:30am'),('07:00am','07:00am'),('07:30am','07:30am'),
        ('08:00am','08:00am'),('08:30am','08:30am'),('09:00am','09:00am'),('09:30am','09:30am'),
        ('10:00am','10:00am'),('10:30am','10:30am'),('11:00am','11:00am'),('11:30am','11:30am'),
        ('12:00pm','12:00pm'),('12:30pm','12:30pm'),('13:00pm','13:00pm'),('13:30pm','13:30pm'),
        ('14:00pm','14:00pm'),('14:30pm','14:30pm'),('15:00pm','15:00pm'),('15:30pm','15:30pm'),
        ('16:00pm','16:00pm'),('16:30pm','16:30pm'),('17:00pm','17:00pm'),('17:30pm','17:30pm'),
        ('18:00pm','18:00pm'),('18:30pm','18:30pm'),('19:00pm','19:00pm'),('19:30pm','19:30pm'),
        ('20:00pm','20:00pm'),('20:30pm','20:30pm'),('21:00pm','21:00pm'),('21:30pm','21:30pm'),
    )
    time_arrival = (
        ('06:00am','06:00am'),('06:30am','06:30am'),('07:00am','07:00am'),('07:30am','07:30am'),
        ('08:00am','08:00am'),('08:30am','08:30am'),('09:00am','09:00am'),('09:30am','09:30am'),
        ('10:00am','10:00am'),('10:30am','10:30am'),('11:00am','11:00am'),('11:30am','11:30am'),
        ('12:00pm','12:00pm'),('12:30pm','12:30pm'),('13:00pm','13:00pm'),('13:30pm','13:30pm'),
        ('14:00pm','14:00pm'),('14:30pm','14:30pm'),('15:00pm','15:00pm'),('15:30pm','15:30pm'),
        ('16:00pm','16:00pm'),('16:30pm','16:30pm'),('17:00pm','17:00pm'),('17:30pm','17:30pm'),
        ('18:00pm','18:00pm'),('18:30pm','18:30pm'),('19:00pm','19:00pm'),('19:30pm','19:30pm'),
        ('20:00pm','20:00pm'),('20:30pm','20:30pm'),('21:00pm','21:00pm'),('21:30pm','21:30pm'),
    )
    plate_Number = models.ForeignKey(BusRegistartion, on_delete = models.CASCADE)
    from_point = models.CharField(max_length=50, choices = form_orign)
    to_point = models.CharField(max_length=50, choices = to_destination)
    departure_date = models.CharField(max_length=50)
    time_of_travel = models.CharField(max_length=50, choices = travell_time)
    company_name = models.CharField(max_length=50)
    arrival_Time = models.CharField(max_length=50, choices = time_arrival)
    driver_name = models.CharField(max_length=50)
    assistant_name = models.CharField(max_length=50)
    amenity1 = models.CharField(max_length=50, choices = amenity_one)
    amenity2 = models.CharField(max_length=50, choices = amenity_two)
    amenity3 = models.CharField(max_length=50, choices = amenity_three)
    amenity4 = models.CharField(max_length=50, choices = amenity_four)
    dail_fare = models.CharField(max_length=50,)
    class Meta:
        verbose_name_plural = "Bus And Routes Registration"
    def __str__(self):
        return self.plate_Number.plate_Number

class CompanyStaff(models.Model):
    staffStatus = (
        ('Receptionist','Receptionist'),
        ('Driver','Driver'),('Assistant','Assistant'),
        ('Cargo-owner','Cargo-owner'),('Administrator','Administrator')
    )
    user = models.OneToOneField(User, related_name='user', on_delete = models.CASCADE)
    company_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)
    staff_status = models.CharField(max_length = 100, choices = staffStatus)
    class Meta:
        verbose_name_plural = "Company Staff"
    def __str__(self):
        return self.user.username
