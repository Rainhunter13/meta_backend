# meta_back [last update: 09.02.2021]
meta_back is a backend application mainly responisble for synchronizing therapists information between Airtable and PostgreSQL databases

## Project structure:
<pre>
.                             
├── configurations                 # project configurations
    ├── __init__.py                                    
├── meta_back                      # project settings    
    ├── __init__.py
    ├── asgi.py                    # ASGI config
    ├── settings.py                # project settings
    ├── urls.py                    # api root router
    └── wsgi.py                    # WSGI config
├── therapists_profiles            # therapists_profiles app
    ├── __init__.py
    ├── migrations/                # app migrations
    ├── scripts/                   # cli and python scripts  
        ├── __init__.py      
        ├── sync.sh                # shell scipt to sync PosgtreSQL from Airtable
        └── sync_script.py         # python script to PosgtreSQL from Airtable
    ├── services/                  # app services
        ├── __init__.py
        └── airtable_services.py   # python script to PosgtreSQL from Airtable
    ├── admin.py                   # registering models here
    ├── apps.py                    # app config
    ├── models.py                  # db models
    ├── test.py                    # app tests
    ├── urls.py                    # urls routing
    └── views.py                   # views
├── .gitignore                     # .gitignore file                 
├── manage.py                      # Django project manager                  
├── README.md                      # <-- you are here                
└── requirements.txt               # Python requirements       
</pre>      

## How to run:

0. Install Python 3.7, pip, PostgreSQL

1. Clone the repository:
```
git clone https://github.com/Rainhunter13/meta_back
```

2. Create PosgtreSQL database

3. Create ```config.py``` in the ```configurations/``` directory and define configuration values in the following format:
```
# Django secret key
secret_key = 'fpog&vp#ldnk*mv_8@w+kimqvbnhbr8=#pz^41s9&*h)y)1gp*'

# PosgtreSQL config
db_name = 'to_fill'
db_user = 'to_fill'
db_password = 'to_fill?'

# Airtable config
base_key = 'to_fill'
api_key = 'to_fill'

```

4. Install python dependencies with the command from the project root directory:
```
pip install requirements.txt
```

5. Run the app:
```
python manage.py runserver
```

## Usage:

### Sync scripts
1. To make PostgreSQL check and apply changes from airtable:
  - go to therapists_profiles/scripts directory and run command ```python sync_script.py```  <br/>
  OR <br/>
  - go to therapists_profiles/scripts directory and run command ```./sync.sh```  <br/>

### REST API endpoints

1. All therapists info:
- Route: ``` /therapists/profiles ```
- Method: GET
- Response: Dictionary of therapists profiles info

2. Specific therapist info (by id in PostgreSQL db):
- Route: ``` /therapists/profiles/{id} ```
- Method: GET
- Response: Dicitionary of therapist profile info

## Implementation details:
When running on of the sync.sh/sync_script.py:
- Authorization to Airtable is done
- Airtable therapists info is compared to that one in PostgreSQL and Postgres updates when needed
- When updating, update record are keeped in SyncRecord table
