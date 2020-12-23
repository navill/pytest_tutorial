import pytest
from django.test import TestCase
from django.contrib.auth.models import Group, User


class MyTest(TestCase):
    fixtures = ['group.json', 'user.json']

    def test_should_create_group(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, 'appusers')

    def test_should_craete_user(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.pk, 1)


@pytest.fixture
def user_A(db):
    return User.objects.create_user('A')


def test_should_create_user_with_username(db, user_A):
    assert user_A.username == 'A'


def test_should_check_password(db, user_A):
    user_A.set_password('secret')
    assert user_A.check_password('secret') is True


def test_should_not_check_unusable_password(db, user_A):
    user_A.set_password('secret')
    user_A.set_unusable_password()
    assert user_A.check_password('secret') is False
