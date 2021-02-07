from airtable import Airtable
from configurations.config import base_key, api_key

airtable = Airtable(base_key=base_key, table_name="Psychotherapists", api_key=api_key)

therapists = []
for therapist in airtable.get_all():
    therapists.append({
        'name': therapist['fields']['Имя'],
        'photo_url': therapist['fields']['Фотография'][0]['url'],
        'methods': therapist['fields']['Методы']
    })
