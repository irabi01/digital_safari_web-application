# Generated by Django 2.1 on 2019-01-04 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusAndRoutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_point', models.CharField(choices=[('Arusha', 'Arusha'), ('Dar es salaam', 'Dar es salaam'), ('Dodoma', 'Dodoma'), ('Morogoro', 'Morogoro'), ('Bukoba', 'Bukoba'), ('Moshi', 'Moshi'), ('Kilimanjaro', 'Kilimanjaro'), ('Singida', 'Singida'), ('Tabora', 'Tabora'), ('Tanga', 'Tanga'), ('Iringa', 'Iringa'), ('Songea', 'Songea'), ('Mbeya', 'Mbeya'), ('Mtwara', 'Mtwara'), ('Ruvuma', 'Ruvuma'), ('Kigoma', 'Kigoma'), ('Mombasa', 'Mombasa'), ('Mwanza', 'Mwanza'), ('Babati', 'Babati'), ('Sumbawanga', 'Sumbawanga')], max_length=50)),
                ('to_point', models.CharField(choices=[('Arusha', 'Arusha'), ('Dar es salaam', 'Dar es salaam'), ('Dodoma', 'Dodoma'), ('Morogoro', 'Morogoro'), ('Bukoba', 'Bukoba'), ('Moshi', 'Moshi'), ('Kilimanjaro', 'Kilimanjaro'), ('Singida', 'Singida'), ('Tabora', 'Tabora'), ('Tanga', 'Tanga'), ('Iringa', 'Iringa'), ('Songea', 'Songea'), ('Mbeya', 'Mbeya'), ('Mtwara', 'Mtwara'), ('Ruvuma', 'Ruvuma'), ('Kigoma', 'Kigoma'), ('Mombasa', 'Mombasa'), ('Mwanza', 'Mwanza'), ('Babati', 'Babati'), ('Sumbawanga', 'Sumbawanga')], max_length=50)),
                ('departure_date', models.CharField(max_length=50)),
                ('time_of_travel', models.CharField(choices=[('06:00am', '06:00am'), ('06:30am', '06:30am'), ('07:00am', '07:00am'), ('07:30am', '07:30am'), ('08:00am', '08:00am'), ('08:30am', '08:30am'), ('09:00am', '09:00am'), ('09:30am', '09:30am'), ('10:00am', '10:00am'), ('10:30am', '10:30am'), ('11:00am', '11:00am'), ('11:30am', '11:30am'), ('12:00pm', '12:00pm'), ('12:30pm', '12:30pm'), ('13:00pm', '13:00pm'), ('13:30pm', '13:30pm'), ('14:00pm', '14:00pm'), ('14:30pm', '14:30pm'), ('15:00pm', '15:00pm'), ('15:30pm', '15:30pm'), ('16:00pm', '16:00pm'), ('16:30pm', '16:30pm'), ('17:00pm', '17:00pm'), ('17:30pm', '17:30pm'), ('18:00pm', '18:00pm'), ('18:30pm', '18:30pm'), ('19:00pm', '19:00pm'), ('19:30pm', '19:30pm'), ('20:00pm', '20:00pm'), ('20:30pm', '20:30pm'), ('21:00pm', '21:00pm'), ('21:30pm', '21:30pm')], max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('arrival_Time', models.CharField(choices=[('06:00am', '06:00am'), ('06:30am', '06:30am'), ('07:00am', '07:00am'), ('07:30am', '07:30am'), ('08:00am', '08:00am'), ('08:30am', '08:30am'), ('09:00am', '09:00am'), ('09:30am', '09:30am'), ('10:00am', '10:00am'), ('10:30am', '10:30am'), ('11:00am', '11:00am'), ('11:30am', '11:30am'), ('12:00pm', '12:00pm'), ('12:30pm', '12:30pm'), ('13:00pm', '13:00pm'), ('13:30pm', '13:30pm'), ('14:00pm', '14:00pm'), ('14:30pm', '14:30pm'), ('15:00pm', '15:00pm'), ('15:30pm', '15:30pm'), ('16:00pm', '16:00pm'), ('16:30pm', '16:30pm'), ('17:00pm', '17:00pm'), ('17:30pm', '17:30pm'), ('18:00pm', '18:00pm'), ('18:30pm', '18:30pm'), ('19:00pm', '19:00pm'), ('19:30pm', '19:30pm'), ('20:00pm', '20:00pm'), ('20:30pm', '20:30pm'), ('21:00pm', '21:00pm'), ('21:30pm', '21:30pm')], max_length=50)),
                ('driver_name', models.CharField(max_length=50)),
                ('assistant_name', models.CharField(max_length=50)),
                ('amenity1', models.CharField(choices=[('Television', 'Television'), ('None', 'None')], max_length=50)),
                ('amenity2', models.CharField(choices=[('Wi-fi', 'Wi-fi'), ('None', 'None')], max_length=50)),
                ('amenity3', models.CharField(choices=[('Charging-service', 'Charging-service'), ('None', 'None')], max_length=50)),
                ('amenity4', models.CharField(choices=[('Drinks', 'Drinks'), ('None', 'None')], max_length=50)),
                ('dail_fare', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Bus And Routes Registration',
            },
        ),
        migrations.CreateModel(
            name='BusRegistartion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_Number', models.CharField(max_length=20)),
                ('seat_Number', models.CharField(max_length=5)),
                ('company_name', models.CharField(max_length=50)),
                ('bus_Type', models.CharField(choices=[('Yutong', 'Yutong'), ('Zhong Tong', 'Zhong Tong'), ('Golden Dragon', 'Golden Dragon')], max_length=50)),
                ('bus_class', models.CharField(choices=[('Luxury', 'Luxury'), ('Semi-Luxury', 'Semi-Luxury'), ('Ordinary', 'Ordinary')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Bus Registartion',
            },
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('tiny_number', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('business_license', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Company Information',
            },
        ),
        migrations.CreateModel(
            name='CompanyStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('staff_status', models.CharField(choices=[('Receptionist', 'Receptionist'), ('Driver', 'Driver'), ('Assistant', 'Assistant'), ('Cargo-owner', 'Cargo-owner'), ('Administrator', 'Administrator')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Company Staff',
            },
        ),
        migrations.AddField(
            model_name='busandroutes',
            name='plate_Number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.BusRegistartion'),
        ),
    ]
