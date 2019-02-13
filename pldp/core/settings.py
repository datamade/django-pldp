SECRET_KEY = 'replacethiswithsomethingsecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'pldp',
        'USER': '',
        'PASSWORD': '',
        'PORT': 5432,
    }
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'countries_plus',
    'languages_plus',
    'pldp.core',
    'pldp.location',
    'pldp.agency',
    'pldp.study',
    'pldp.survey',
)

MIDDLEWARE_CLASSES = ()