import pytest

from car_rent.models import CustomUser


@pytest.fixture()
def user_1(db):
    user = CustomUser.objects.create_user("test@user.pl", 'password')
    return user


@pytest.mark.django_db
def test_set_check_password(user_1):
    assert user_1.email == "test@user.pl"
