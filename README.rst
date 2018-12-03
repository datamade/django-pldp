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
)
```

Load in necessary fixtures

```
python manage.py initialize_pldp
```

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
