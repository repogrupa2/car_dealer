# Generated by Django 4.0.6 on 2022-08-06 13:09

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchcaravailability',
            old_name='Branch_Id',
            new_name='branch_id',
        ),
        migrations.RenameField(
            model_name='branchcaravailability',
            old_name='Vehicle_Id',
            new_name='vehicle_id',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='opening_hours',
        ),
        migrations.AddField(
            model_name='branch',
            name='open_from',
            field=models.CharField(choices=[('00', '00:00'), ('01', '01:00'), ('02', '02:00'), ('03', '03:00'), ('04', '04:00'), ('05', '05:00'), ('06', '06:00'), ('07', '07:00'), ('08', '08:00'), ('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='open_till',
            field=models.CharField(choices=[('00', '00:00'), ('01', '01:00'), ('02', '02:00'), ('03', '03:00'), ('04', '04:00'), ('05', '05:00'), ('06', '06:00'), ('07', '07:00'), ('08', '08:00'), ('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='branch',
            name='mobile',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+00 000 000 000'. Up to 11 digits allowed.", regex='(^[+]\\d+(?:[ ]\\d+)*)')]),
        ),
    ]