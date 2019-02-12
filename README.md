# django-pldp

🌳 A reusable Django app implementing the Gehl Institute's [Public Life Data Protocol](https://gehlinstitute.org/tool/public-life-data-protocol/).

## Philosophical underpinnings

From the [Gehl Institute](https://gehlinstitute.org/):

> The Public Life Data Protocol (the Protocol) describes a set of metrics that
> are important to the understanding of public life—people moving and staying
> in public space—and aims to establish a common format for the collection and
> storage of such data. Used in conjunction with the Public Life Data Tools or
> other observational methods for collecting data about people in public space,
> the Protocol provides the structure for the data you collect.

> Based on four decades of research and application of data about public life
> to shape public policy, planning, and urban design, the Protocol is an open
> data specification intended to improve the ability of everyone to share and
> compare information about public life activity in public space. In recent
> years, practitioners and cities have incorporated people-centered metrics and
> public life data into their engineering models, investment decisions, and
> design choices. These methods, based on decades of research, have now been
> applied in hundreds of cities around the world. There is tremendous potential
> to make public life datasets more compatible, scalable, and comparable across
> different cities and regions.

The PLDP describes 3 different modes of collecting observational survey data:

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

This implementation of the PLDP is based on the September 2017 Beta release. The Gehl
Institute's full documentation of the protocol can be found [here](pldp-source-documents/PLDP_BETA%20Publication%20-%2020170927.pdf).

## Adding `django-pldp` to your project (NB: this needs work)

1. Add django-pldp to the installed apps in your project's settings.py file:

```python
INSTALLED_APPS = (
    ...
    'countries_plus',
    'languages_plus',
    'pldp',
)
```

4. Update migrations:

`python manage.py migrate`

5. Load in necessary fixtures from `django-pldp`:

```
python manage.py initialize_pldp
```

You should now be able to use `django-pldp` in your project!

## Developing `django-pldp` locally

1. Clone this repository and `cd` into your local copy.

    ```bash
    git clone git@github.com:datamade/django-pldp.git
    cd django-pldp
    ```

2. Create a virtual environment. (We recommend using [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) for working in a virtualized development environment.)

    ```bash
    mkvirtualenv -p python3 pldp
    ```

3. Install the requirements.

    ```bash
    pip install -r pldp/requirements.txt
    ```

4. Export the Django settings:

`export DJANGO_SETTINGS_MODULE=tests.test_config`

4. Create a database:

`createdb pldp`

5. Run migrations:

`django-admin migrate`


## Copyright

Copyright (c) 2019 University City District and DataMade.
Released under the [MIT
License](https://github.com/datamade/django-councilmatic/blob/master/LICENSE).
