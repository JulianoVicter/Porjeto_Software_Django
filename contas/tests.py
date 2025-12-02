from django.test import SimpleTestCase
from django.urls import resolve, reverse

from . import views


class ContasURLTests(SimpleTestCase):
    def test_login_url_points_to_shared_view(self):
        url = reverse("login")
        self.assertEqual(url, "/contas/login/")
        self.assertIs(resolve(url).func, views.login)

    def test_login_ong_url_points_to_shared_view(self):
        url = reverse("login_ong")
        self.assertEqual(url, "/contas/login/ong/")
        self.assertIs(resolve(url).func, views.login)
