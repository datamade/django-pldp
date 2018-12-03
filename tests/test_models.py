import pytest

from countries_plus.models import Country
from pldp.agency.models import Agency

@pytest.fixture
@pytest.mark.django_db
def countries(db):
    call_command('update_countries_plus')


@pytest.fixture
def country(countries):
    return Country.objects.order_by('?').first()


@pytest.fixture
def agency():
    agency = Agency.objects.create(name='Test Agency',
                                   email='test@testagency.com')
    return agency


@pytest.fixture
def location_line():
    linestring = {
        "type": "LineString",
        "coordinates": [
            [
                -101.744384,
                39.32155
            ],
            [
                -101.552124,
                39.330048
            ],
            [
                -101.403808,
                39.330048
            ],
            [
                -101.332397,
                39.364032
            ],
        ]
    }
    return LocationLine.objects.create(geometry=linestring,
                                       date_measured='2018/11/11')

@pytest.fixture
def location(agency, country, location_line):
    location = Location.objects.create(agency=agency,
                                       country=country,
                                       primary_name='Test location',
                                       line=location_line)
    return location
