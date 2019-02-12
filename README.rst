django-pldp
===========

Reusable Django app that implements the structure implied by the PDLP.

To develop `django-pldp` locally
-----

1. Create a virtualenv:

2. Install requirements:

`pip install -r pldp/requirements.txt`

3. Export Django settings:

`export DJANGO_SETTINGS_MODULE=tests.test_config`

4. Create a database:

`createdb pldp`

5. Run migrations:

`django-admin migrate`


To add `django-pldp` to your project
-----

1. Add django-pldp to the installed apps in your project's settings.py file:

```python
INSTALLED_APPS = [
    ...
    'countries_plus',
    'languages_plus',
    'pldp.core',
]
```

4. Update migrations:

`python manage.py migrate`

5. Load in necessary fixtures from `django-pldp`:

```
python manage.py initialize_pldp
```

You should now be able to use `django-pldp` in your project!

Philosophical underpinnings
---------------------------

PLDP describes 3 different modes of collecting survey responses:

1. Linked surveys: Collecting many pieces of information at the same time
   about the same respondents.
2. Simultaneous surveys: Collecting many pieces of information at the same
   time but not about the same respondents.
3. Consecutive surveys: Collecting many pieces of information at different
   times from different respondents.

Surveys should always have a Study and Location in common. A Survey in the
first mode has a collection of SurveyComponents that share a SurveyRow.
A Survey in the second mode can have a collection of SurveyComponents but they
will each be in separate SurveyRow. The third mode suggests entirely disjoint
collection efforts that merely have a Location in common.

Copyright
---------

Copyright (c) 2018 University City District and DataMade.
Released under the `MIT
License <https://github.com/datamade/django-councilmatic/blob/master/LICENSE>`__.
