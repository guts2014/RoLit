"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import json
from django.test import TestCase, TransactionTestCase, Client
from django.core.urlresolvers import reverse
from models import Telemetry
from datetime import datetime

# --- Tests for the adding function ---
class AddValuesTest1(TestCase):
    def test_add(self):
        url = reverse('add_values')
        client = Client()
        response = client.post(url)

        self.assertEqual(response.status_code, 200)

class AddValuesTest2(TestCase):
    def test_add(self):
        url = reverse('add_values')
        client = Client()
        response = client.post(url, test_data)

        self.assertEqual(response.status_code, 200)

# --- Tests for the function that retrieves the latest values. ---
class GetLatestValuesTest1(TestCase):
    def setUp(self):
        # Add an extra object to make sure we are getting the latest.
        Telemetry.objects.create(
            report_datetime=datetime.now(),
            battery=test_data['BATTERY'] * 2,
			brake=test_data['BRAKE'] * 2,
			coolant_t=test_data['COOLANT_T'] * 2,
			fuel=test_data['FUEL'] * 2,
			gear=test_data['GEAR'] * 2,
			map=test_data['MAP'] * 2,
			mat=test_data['MAT'] * 2,
			o2=test_data['O2'] * 2,
			rpm=test_data['RPM'] * 2,
			speed=test_data['SPEED'] * 2,
			throttle=test_data['THROTTLE'] * 2,
			wheel_t_1=test_data['WHEEL_T_1'] * 2,
			wheel_t_2=test_data['WHEEL_T_2'] * 2,
			wheel_t_3=test_data['WHEEL_T_3'] * 2,
			wheel_t_4=test_data['WHEEL_T_4'] * 2,
			wheel_v_1=test_data['WHEEL_V_1'] * 2,
			wheel_v_2=test_data['WHEEL_V_2'] * 2,
			wheel_v_3=test_data['WHEEL_V_3'] * 2,
			wheel_v_4=test_data['WHEEL_V_4'] * 2,
        )

        # This is the data that should be considered latest.
        Telemetry.objects.create(
            report_datetime=datetime.now(),
            battery=test_data['BATTERY'],
			brake=test_data['BRAKE'],
			coolant_t=test_data['COOLANT_T'],
			fuel=test_data['FUEL'],
			gear=test_data['GEAR'],
			map=test_data['MAP'],
			mat=test_data['MAT'],
			o2=test_data['O2'],
			rpm=test_data['RPM'],
			speed=test_data['SPEED'],
			throttle=test_data['THROTTLE'],
			wheel_t_1=test_data['WHEEL_T_1'],
			wheel_t_2=test_data['WHEEL_T_2'],
			wheel_t_3=test_data['WHEEL_T_3'],
			wheel_t_4=test_data['WHEEL_T_4'],
			wheel_v_1=test_data['WHEEL_V_1'],
			wheel_v_2=test_data['WHEEL_V_2'],
			wheel_v_3=test_data['WHEEL_V_3'],
			wheel_v_4=test_data['WHEEL_V_4'],
        )

    def test_get(self):
        url = reverse('get_latest_values')
        client = Client()
        response = client.post(url)
        json_data = json.loads(response.content)

        # Do the assertions.
        self.assertIsNotNone(json_data['id'])
        self.assertIsNotNone(json_data['report_datetime'])
        self.assertEqual(json_data['battery'], test_data['BATTERY'])
        self.assertEqual(json_data['brake'], test_data['BRAKE'])
        self.assertEqual(json_data['coolant_t'], test_data['COOLANT_T'])
        self.assertEqual(json_data['fuel'], test_data['FUEL'])
        self.assertEqual(json_data['gear'], test_data['GEAR'])
        self.assertEqual(json_data['map'], test_data['MAP'])
        self.assertEqual(json_data['mat'], test_data['MAT'])
        self.assertEqual(json_data['o2'], test_data['O2'])
        self.assertEqual(json_data['rpm'], test_data['RPM'])
        self.assertEqual(json_data['speed'], test_data['SPEED'])
        self.assertEqual(json_data['throttle'], test_data['THROTTLE'])
        self.assertEqual(json_data['wheel_t_1'], test_data['WHEEL_T_1'])
        self.assertEqual(json_data['wheel_t_2'], test_data['WHEEL_T_2'])
        self.assertEqual(json_data['wheel_t_3'], test_data['WHEEL_T_3'])
        self.assertEqual(json_data['wheel_t_4'], test_data['WHEEL_T_4'])
        self.assertEqual(json_data['wheel_v_1'], test_data['WHEEL_V_1'])
        self.assertEqual(json_data['wheel_v_2'], test_data['WHEEL_V_2'])
        self.assertEqual(json_data['wheel_v_3'], test_data['WHEEL_V_3'])
        self.assertEqual(json_data['wheel_v_4'], test_data['WHEEL_V_4'])

class GetLatestValuesTest2(TestCase):
    def setUp(self):
        # Add an extra object to make sure we are getting the latest.
        Telemetry.objects.create(
            report_datetime=datetime.now(),
            battery=test_data['BATTERY'],
			brake=test_data['BRAKE'],
			coolant_t=test_data['COOLANT_T'],
			fuel=test_data['FUEL'],
			gear=test_data['GEAR'],
			map=test_data['MAP'],
			mat=test_data['MAT'],
			o2=test_data['O2'],
			rpm=test_data['RPM'],
			speed=test_data['SPEED'],
			throttle=test_data['THROTTLE'],
			wheel_t_1=test_data['WHEEL_T_1'],
			wheel_t_2=test_data['WHEEL_T_2'],
			wheel_t_3=test_data['WHEEL_T_3'],
			wheel_t_4=test_data['WHEEL_T_4'],
			wheel_v_1=test_data['WHEEL_V_1'],
			wheel_v_2=test_data['WHEEL_V_2'],
			wheel_v_3=test_data['WHEEL_V_3'],
			wheel_v_4=test_data['WHEEL_V_4'],
        )

        # This is the data that should be considered latest.
        Telemetry.objects.create(
            report_datetime=datetime.now(),
        )

    def test_get(self):
        url = reverse('get_latest_values')
        client = Client()
        response = client.post(url, test_data)
        json_data = json.loads(response.content)

        # Do the assertions.
        self.assertIsNotNone(json_data['id'])
        self.assertIsNotNone(json_data['report_datetime'])
        self.assertIsNone(json_data['battery'])
        self.assertIsNone(json_data['brake'])
        self.assertIsNone(json_data['coolant_t'])
        self.assertIsNone(json_data['fuel'])
        self.assertIsNone(json_data['gear'])
        self.assertIsNone(json_data['map'])
        self.assertIsNone(json_data['mat'])
        self.assertIsNone(json_data['o2'])
        self.assertIsNone(json_data['rpm'])
        self.assertIsNone(json_data['speed'])
        self.assertIsNone(json_data['throttle'])
        self.assertIsNone(json_data['wheel_t_1'])
        self.assertIsNone(json_data['wheel_t_2'])
        self.assertIsNone(json_data['wheel_t_3'])
        self.assertIsNone(json_data['wheel_t_4'])
        self.assertIsNone(json_data['wheel_v_1'])
        self.assertIsNone(json_data['wheel_v_2'])
        self.assertIsNone(json_data['wheel_v_3'])
        self.assertIsNone(json_data['wheel_v_4'])

# --- Tests for the function that retrieves values by id. ---
class GetValuesById(TransactionTestCase):
    def setUp(self):
        # This is the data that should be under id 1.
        Telemetry.objects.create(
            report_datetime=datetime.now(),
            battery=test_data['BATTERY'],
			brake=test_data['BRAKE'],
			coolant_t=test_data['COOLANT_T'],
			fuel=test_data['FUEL'],
			gear=test_data['GEAR'],
			map=test_data['MAP'],
			mat=test_data['MAT'],
			o2=test_data['O2'],
			rpm=test_data['RPM'],
			speed=test_data['SPEED'],
			throttle=test_data['THROTTLE'],
			wheel_t_1=test_data['WHEEL_T_1'],
			wheel_t_2=test_data['WHEEL_T_2'],
			wheel_t_3=test_data['WHEEL_T_3'],
			wheel_t_4=test_data['WHEEL_T_4'],
			wheel_v_1=test_data['WHEEL_V_1'],
			wheel_v_2=test_data['WHEEL_V_2'],
			wheel_v_3=test_data['WHEEL_V_3'],
			wheel_v_4=test_data['WHEEL_V_4'],
        )

        # This is the data that should be under id 2.
        Telemetry.objects.create(
            report_datetime=datetime.now(),
        )

    def test_get(self):
        url = reverse('get_values_by_id')
        client = Client()

        latest_id = Telemetry.objects.latest('id').id
        print ">>Latest ID: " + str(latest_id)

        # Get the first set of values.
        response = client.post(url, {'ID': latest_id - 1})
        json_data = json.loads(response.content)

        # Do the first set of assertions.
        self.assertIsNotNone(json_data['id'])
        self.assertEqual(json_data['id'], latest_id - 1)
        self.assertIsNotNone(json_data['report_datetime'])
        self.assertEqual(json_data['battery'], test_data['BATTERY'])
        self.assertEqual(json_data['brake'], test_data['BRAKE'])
        self.assertEqual(json_data['coolant_t'], test_data['COOLANT_T'])
        self.assertEqual(json_data['fuel'], test_data['FUEL'])
        self.assertEqual(json_data['gear'], test_data['GEAR'])
        self.assertEqual(json_data['map'], test_data['MAP'])
        self.assertEqual(json_data['mat'], test_data['MAT'])
        self.assertEqual(json_data['o2'], test_data['O2'])
        self.assertEqual(json_data['rpm'], test_data['RPM'])
        self.assertEqual(json_data['speed'], test_data['SPEED'])
        self.assertEqual(json_data['throttle'], test_data['THROTTLE'])
        self.assertEqual(json_data['wheel_t_1'], test_data['WHEEL_T_1'])
        self.assertEqual(json_data['wheel_t_2'], test_data['WHEEL_T_2'])
        self.assertEqual(json_data['wheel_t_3'], test_data['WHEEL_T_3'])
        self.assertEqual(json_data['wheel_t_4'], test_data['WHEEL_T_4'])
        self.assertEqual(json_data['wheel_v_1'], test_data['WHEEL_V_1'])
        self.assertEqual(json_data['wheel_v_2'], test_data['WHEEL_V_2'])
        self.assertEqual(json_data['wheel_v_3'], test_data['WHEEL_V_3'])
        self.assertEqual(json_data['wheel_v_4'], test_data['WHEEL_V_4'])

        # Get the first set of values.
        response = client.post(url, {'ID': latest_id})
        json_data = json.loads(response.content)

        # Do the second set of assertions.
        self.assertIsNotNone(json_data['id'])
        self.assertEqual(json_data['id'], latest_id)
        self.assertIsNotNone(json_data['report_datetime'])
        self.assertIsNone(json_data['battery'])
        self.assertIsNone(json_data['brake'])
        self.assertIsNone(json_data['coolant_t'])
        self.assertIsNone(json_data['fuel'])
        self.assertIsNone(json_data['gear'])
        self.assertIsNone(json_data['map'])
        self.assertIsNone(json_data['mat'])
        self.assertIsNone(json_data['o2'])
        self.assertIsNone(json_data['rpm'])
        self.assertIsNone(json_data['speed'])
        self.assertIsNone(json_data['throttle'])
        self.assertIsNone(json_data['wheel_t_1'])
        self.assertIsNone(json_data['wheel_t_2'])
        self.assertIsNone(json_data['wheel_t_3'])
        self.assertIsNone(json_data['wheel_t_4'])
        self.assertIsNone(json_data['wheel_v_1'])
        self.assertIsNone(json_data['wheel_v_2'])
        self.assertIsNone(json_data['wheel_v_3'])
        self.assertIsNone(json_data['wheel_v_4'])

# --- Dummy data used for testing. ---
test_data = {
    'BATTERY': 1.1,
    'BRAKE': 2.2,
    'COOLANT_T': 3.3,
    'FUEL': 4.4,
    'GEAR': 5.5,
    'MAP': 6.6,
    'MAT': 7.7,
    'O2': 8.8,
    'RPM': 9.9,
    'SPEED': 10.0,
    'THROTTLE': 11.1,
    'WHEEL_T_1': 12.2,
    'WHEEL_T_2': 13.3,
    'WHEEL_T_3': 14.4,
    'WHEEL_T_4': 15.5,
    'WHEEL_V_1': 16.6,
    'WHEEL_V_2': 17.7,
    'WHEEL_V_3': 18.8,
    'WHEEL_V_4': 19.9,
    }