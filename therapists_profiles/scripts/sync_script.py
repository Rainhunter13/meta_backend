"""Python script that synchronize Airtable with PostgreSQL"""
import sys
import os
import django

sys.path.append("/home/rainhunter/PycharmProjects/meta_fullstack")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meta_fullstack.settings")
django.setup()

from therapists_profiles.services.airtable_services import AirtableService

airtable_service = AirtableService('Psychotherapists')
airtable_service.sync_airtable_with_postgres()
