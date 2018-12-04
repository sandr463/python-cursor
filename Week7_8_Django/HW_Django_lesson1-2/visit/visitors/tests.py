from django.test import TestCase, Client
from django.urls import reverse

from visitors.models import Visitor


class VisitorAddViewTest(TestCase):
    def setUp(self):
        client = Client()

    def test_visitor_added(self):
        """Test if Added visitor saved in database """
        response = self.client.post(reverse('add_visitor'), {'name': 'admin', 'age': 123, 'some_info': 'qwerty'})
        self.assertEqual(response.status_code, 302)


class VisitorUpdateViewTest(TestCase):
    def setUp(self):
        client = Client()
        self.name = 'test'
        self.age = 123
        self.some_info = 'qwe'
        self.id = 1000

    def test_update_visitor(self):
        """Testing visitors updateview"""
        visitor = Visitor.objects.create(age=122)

        response = self.client.post(
            reverse('update_visitor', kwargs={'pk': visitor.id}),
            {'name': 'Test', 'age': 123, 'some_info': 'qwerty'})

        self.assertEqual(response.status_code, 302)

        visitor.refresh_from_db()
        self.assertEqual(visitor.age, 123)


class VisitorDeleteViewTest(TestCase):
    def setUp(self):
        client = Client()

    def test_visitor_delete(self):
        """Testing visitors deleteview"""
        visitor = Visitor.objects.create(age=12, some_info='qwe')
        response = self.client.post(reverse('delete_visitor', kwargs={'pk': visitor.pk}))
        self.assertEqual(response.status_code, 302)


class VisitorLoginViewTest(TestCase):
    def setUp(self):
        client = Client()

    def test_visitor_login(self):
        """Testing VisitorLoginView"""
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)


class VisitorLogoutViewTest(TestCase):
    def setUp(self):
        client = Client()

    def test_visitor_logout(self):
        """Testing VisitorLogoutView"""
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
