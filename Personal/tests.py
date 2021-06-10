#django modules
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'username', 'lastname', '2021-03-03', 4000, 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.last_name, 'lastname')
        self.assertEqual(super_user.start_date, '2021-03-03')
        self.assertEqual(super_user.salary, 4000)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', last_name='first_name', start_date='2021-03-03', position='Gerencia', salary=2000, password='password', is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', last_name='first_name', start_date='2021-03-03', position='Gerencia', salary=2000, password='password', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='username1', last_name='first_name', start_date='2021-03-03', position='Gerencia', salary=2000, password='password', is_superuser=True)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@super.com', 'username', 'lastname', '2021-03-03', 'Gerencia', 4000, 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.last_name, 'lastname')
        self.assertEqual(user.start_date, '2021-03-03')
        self.assertEqual(user.area, 'Gerencia')
        self.assertEqual(user.salary, 4000)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', user_name='username1', last_name='first_name', start_date='2021-03-03', area='Contabilidad', salary=2000, password='password')