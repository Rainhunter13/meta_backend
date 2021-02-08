"""Services for working with data from airtable"""

from datetime import date
from airtable import Airtable

from configurations.config import base_key, api_key
from therapists_profiles.models import SyncRecord, Therapist, Method


class AirtableService:
    """Airtable Service"""
    table_name = ""

    def __init__(self, table_name):
        """Defines Airtable table name"""
        self.table_name = table_name

    def authenticate_airtable(self):
        """Authenticate Airtable table"""
        airtable = Airtable(base_key=base_key, table_name=self.table_name, api_key=api_key)
        return airtable

    def get_therapists_from_airtable(self):
        """Returns a list of therapists in the airtable"""
        airtable = self.authenticate_airtable()

        therapists_dicts = []
        for airtable_therapist in airtable.get_all():
            therapists_dicts.append({
                'airtable_id': airtable_therapist['id'],
                'name': airtable_therapist['fields']['Имя'],
                'photo_url': airtable_therapist['fields']['Фотография'][0]['url'],
                'methods': airtable_therapist['fields']['Методы']
            })

        return therapists_dicts

    def sync_airtable_with_postgres(self):
        """Make changes in PostgreSQL database so that therapist list is
        same as in Airtable and adds respective synchronize record """
        therapists_dicts = self.get_therapists_from_airtable()
        airtable_ids = set()

        sync_record = SyncRecord(date=date.today())
        sync_record.save()

        for therapist_dict in therapists_dicts:
            airtable_ids.add(therapist_dict['airtable_id'])
            if not Therapist.objects.filter(airtable_id=therapist_dict['airtable_id']):
                add_therapist_to_postgres(therapist_dict, sync_record)
            else:
                update_therapist_in_postgres(therapist_dict, sync_record)

        for therapist in Therapist.objects.all():
            if therapist.airtable_id not in airtable_ids:
                therapist.delete()


def add_therapist_to_postgres(therapist_dict, sync_record):
    """Adds a new therapist to PostgreSQL database"""
    new_therapist = Therapist(
        airtable_id=therapist_dict['airtable_id'],
        name=therapist_dict['name'],
        photo_url=therapist_dict['photo_url']
    )
    new_therapist.save()
    new_therapist.sync_record.add(sync_record)

    for method_name in therapist_dict['methods']:
        if not Method.objects.filter(name=method_name):
            new_method = Method(name=method_name)
            new_method.save()
            new_method.therapist.add(new_therapist)
        else:
            method = Method.objects.get(name=method_name)
            method.therapist.add(new_therapist)


def update_therapist_in_postgres(therapist_dict, sync_record):
    """Updates therapist fields in PostgreSQL database"""
    old_therapist = Therapist.objects.get(airtable_id=therapist_dict['airtable_id'])
    old_therapist.name = therapist_dict['name']
    old_therapist.photo_url = therapist_dict['photo_url']
    old_therapist.sync_record.add(sync_record)

    for method_name in therapist_dict['methods']:
        if not Method.objects.filter(name=method_name):
            new_method = Method(name=method_name)
            new_method.save()
            new_method.therapist.add(old_therapist)
        else:
            method = Method.objects.get(name=method_name)
            if old_therapist not in method.therapist.all():
                method.therapist.add(old_therapist)
