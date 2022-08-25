# Generated by Django 4.0.6 on 2022-08-25 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0015_alter_rentaloffer_vehicle_id_alter_vehicle_engine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='city',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Must be clear text ', regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Must be clear text ', regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='CVV',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Must be clear text ', regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='expiration',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='street',
            field=models.CharField(max_length=39, null=True, validators=[django.core.validators.RegexValidator(message='Must be clear text ', regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Must be clear text ', regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='rentaloffer',
            name='Categories',
            field=models.CharField(choices=[('Economy', 'Economy'), ('Intermediate ', 'Intermediate '), ('Premium', 'Premium'), ('Luxury', 'Luxury')], max_length=13, validators=[django.core.validators.RegexValidator(message='Must be clear text ', regex='[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='rentaloffer',
            name='Deposit',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999.99)]),
        ),
        migrations.AlterField(
            model_name='rentaloffer',
            name='Price_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999.99)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='prod_year',
            field=models.SmallIntegerField(max_length=4, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]