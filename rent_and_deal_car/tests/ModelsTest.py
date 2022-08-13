import pytest

from car_rent.models import Vehicle


@pytest.mark.parametrize(
    'body_type, prod_year, color, engine, type_of_fuel,transmission, vin, photo',
    [
        ('Combi', '2014', 'black', '2,0', 'gasoline', 'automatic',
         'WAUZZZ8413212467', 'image')
    ],
)
def test_vehicle_instance(
        db, body_type, prod_year, color, engine, type_of_fuel,
        transmission, vin, photo
):
    test = Vehicle(
        body_type=body_type,
        prod_year=prod_year,
        color=color,
        engine=engine,
        type_of_fuel=type_of_fuel,
        transmission=transmission,
        vin=vin,
        photo=photo,
    )