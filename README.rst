django-pldp
===========

Reusable Django app that implements the structure implied by the PDLP.

Setup
-----

Add necessary things to your installed apps:

```
INSTALLED_APPS = (
    ...
    'languages_plus',
    'pldp',
    'pldp.agency',
    'pldp.study',
    'pldp.location',
    'pldp.survey',

)
```

Load in necessary fixtures

```
python manage.py initialize_pldp
```

Copyright
---------

Copyright (c) 2018 University City District and DataMade.
Released under the `MIT
License <https://github.com/datamade/django-councilmatic/blob/master/LICENSE>`__.
