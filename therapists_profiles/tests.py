"""therapists_profiles app tests"""

import os
import django
from django.test import TestCase

from therapists_profiles.services.airtable_services import get_therapists_from_airtable
from therapists_profiles.services.airtable_services import sync_airtable_with_postgres
from therapists_profiles.models import Therapist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meta_fullstack.settings")
django.setup()


def fill_test_table(airtable):
    """fills test airtable with test values"""
    airtable.insert({
        'Имя': 'Test_Name',
        'Методы': ['test_method_1', 'test_method_2'],
    })


def clear_test_table(airtable):
    """clears test airtable"""
    for record in airtable.get_all():
        airtable.delete(record['id'])


class AirtableTestCase(TestCase):
    """Class for testing airtable services"""

    def test_get_therapists_from_airtable(self):
        """Test for get_therapists_from_airtable()"""
        airtable_therapists = get_therapists_from_airtable('Test_Table')
        self.assertEqual(airtable_therapists[0]['name'], 'Test_Name')

    def test_sync_airtable_with_postgres(self):
        """Test for sync_airtable_with_postgres()"""
        sync_airtable_with_postgres('Test_Table')
        self.assertEqual(Therapist.objects.first().name, 'Test_Name')
