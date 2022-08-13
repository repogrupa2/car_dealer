import pytest

from car_rent.models import CustomUser


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user('test', 'test@test.com', 'test2')
    count = CustomUser.objects.all().count()
    print(count)
    assert CustomUser.objects.count() == 1


@pytest.mark.django_db
def test_user_create():
    count = CustomUser.objects.all().count()
    assert count == 0


