# Generated by Django 4.0.6 on 2022-08-13 09:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('address', models.CharField(max_length=39)),
                ('company', models.CharField(max_length=50, null=True)),
                ('credit_card_nr', models.IntegerField(null=True)),
                ('tax_id', models.CharField(max_length=10, null=True)),
                ('mobile', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone nr must be entered in the format: +00 000 000 000'. Up to 11 digits allowed.", regex='(^[+]\\d+(?:[ ]\\d+)*)')])),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=39)),
                ('city', models.CharField(max_length=16)),
                ('mobile', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+00 000 000 000'. Up to 11 digits allowed.", regex='(^[+]\\d+(?:[ ]\\d+)*)')])),
                ('open_from', models.CharField(choices=[('00', '00:00'), ('01', '01:00'), ('02', '02:00'), ('03', '03:00'), ('04', '04:00'), ('05', '05:00'), ('06', '06:00'), ('07', '07:00'), ('08', '08:00'), ('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], max_length=6)),
                ('open_till', models.CharField(choices=[('00', '00:00'), ('01', '01:00'), ('02', '02:00'), ('03', '03:00'), ('04', '04:00'), ('05', '05:00'), ('06', '06:00'), ('07', '07:00'), ('08', '08:00'), ('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], max_length=6)),
                ('mail', models.EmailField(max_length=39)),
                ('remarks', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BranchCarAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(default=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.CharField(choices=[('Sedan', 'Sedan'), ('Combi', 'Combi'), ('SUV', 'SUV'), ('Sport', 'Sport')], max_length=16)),
                ('prod_year', models.CharField(max_length=4)),
                ('color', models.CharField(max_length=16)),
                ('engine', models.DecimalField(decimal_places=1, max_digits=2)),
                ('type_of_fuel', models.CharField(choices=[('Diesel', 'Diesel'), ('Gasoline', 'Gasoline'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=16)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=16)),
                ('vin', models.CharField(max_length=17)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.model')),
            ],
        ),
        migrations.CreateModel(
            name='RentalOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categories', models.CharField(choices=[('Economy', 'Economy'), ('Intermediate ', 'Intermediate '), ('Premium', 'Premium'), ('Luxury', 'Luxury')], max_length=13)),
                ('Description', models.TextField(null=True)),
                ('Deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BranchCarAvailability_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.branchcaravailability')),
                ('Vehicle_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='CarRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('date_of_rent', models.DateField(auto_now_add=True)),
                ('is_rented', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('rental_offer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.rentaloffer')),
            ],
        ),
        migrations.AddField(
            model_name='branchcaravailability',
            name='vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_rent.vehicle'),
        ),
    ]
