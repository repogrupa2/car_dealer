# Generated by Django 4.0.6 on 2022-08-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0012_remove_rentaloffer_branchcaravailability_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10, null=True),
        ),
    ]
