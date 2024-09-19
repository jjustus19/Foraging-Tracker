from django.test import TestCase
from django.test import Client
from folium import (Marker, Map)


class AcceptanceTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.map = Map(location=(0, 0), zoom_start=3)
        self.map.save()
        self.marker = Marker(location=(43.07836095706915, -87.8819686)).add_to(self.map)
        self.marker.save()

    def test_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_map(self):
        response = self.client.get('')
        self.assertContains(response, self.map)

    def test_map_marker(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.marker.icon)

    def test_client_sees_correct_markers(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        test_marker = Marker(location=(43.07836095706915, -87.8819686)).add_to(self.map)
        self.assertEqual(self.marker.location, test_marker.location)

    def test_non_account_to_login(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

        if not self.client.is_authenticated:
            self.assertContains(response, 'name="login"')
            response = self.client.get('/login/')
            self.assertEqual(response.status_code, 200)
