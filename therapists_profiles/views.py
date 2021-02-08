"""Url views"""

from django.http import HttpResponse
from therapists_profiles.models import Therapist


def profiles(request):
    """Returns a list of therapist in database as a list of dictionaries"""
    therapists = []
    for therapist in Therapist.objects.all():
        methods = []
        for method in therapist.methods.all():
            methods.append(method.name)
        therapists.append({
            'id': therapist.id,
            'name': therapist.name,
            'photo_url': therapist.photo_url,
            'methods': methods,
            'airtable_id': therapist.airtable_id,
        })
    return HttpResponse(therapists)
