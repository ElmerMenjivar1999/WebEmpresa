from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user('test','prueba@prueba.com','test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username ='test').exists()
        self.assertEqual(exists,True)

