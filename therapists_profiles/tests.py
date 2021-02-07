import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meta_fullstack.settings")
django.setup()


def clear_test_table(airtable):
    for record in airtable.get_all():
        airtable.delete(record['id'])


def fill_test_table(airtable):
    airtable.insert({
        'Имя': 'Test_Name',
        'Методы': ['test_method_1', 'test_method_2'],
    })


def test_get_therapists_from_airtable():
    from therapists_profiles.services.airtable_services import get_therapists_from_airtable
    airtable_therapists = get_therapists_from_airtable('Test_Table')
    assert airtable_therapists[0]['name'] == 'Test_Name'


def test_sync_airtable_with_postgres():
    from therapists_profiles.services.airtable_services import sync_airtable_with_postgres
    from therapists_profiles.models import Therapist
    sync_airtable_with_postgres('Test_Table')
    assert Therapist.objects.first().name == 'Test_Name'
    sync_airtable_with_postgres('Psychotherapists')
