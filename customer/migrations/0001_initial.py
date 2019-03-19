# Generated by Django 2.1 on 2019-01-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('boarding_point', models.CharField(max_length=50)),
                ('droping_point', models.CharField(max_length=50)),
                ('seatnumber', models.CharField(max_length=50)),
                ('nauli', models.CharField(max_length=50)),
                ('secretecode', models.CharField(max_length=20)),
                ('ticket_number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'passengers details',
            },
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=50)),
                ('refence_number', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=50)),
                ('emailaddress', models.EmailField(max_length=100)),
                ('secrete_code', models.CharField(max_length=100)),
                ('totalseats', models.CharField(max_length=3)),
                ('amount_total', models.IntegerField()),
                ('from_p', models.CharField(max_length=50)),
                ('to_d', models.CharField(max_length=50)),
                ('date_of_t', models.CharField(max_length=30)),
                ('time_of_t', models.CharField(max_length=20)),
                ('plate_n', models.CharField(max_length=20)),
                ('operator', models.CharField(max_length=50)),
                ('arrivaltime', models.CharField(max_length=20)),
                ('bustype', models.CharField(max_length=20)),
                ('busclass', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'payment information',
            },
        ),
    ]
