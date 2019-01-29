import pytest

from django.core.management import call_command

from countries_plus.models import Country
from pldp.agency.models import Agency
from pldp.survey.models import Survey
from pldp.study.models import StudyArea, Study
from pldp.location.models import Location, LocationLine


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
    linestring = 'LINESTRING(-101.744384 39.32155, -101.552124 39.330048, -101.403808 39.330048, -101.332397 39.364032)'
    return LocationLine.objects.create(geometry=linestring,
                                       date_measured='2018-11-11')


@pytest.fixture
def location(agency, country, location_line):
    location = Location.objects.create(agency=agency,
                                       country=country,
                                       primary_name='Test location',
                                       line=location_line)
    return location


@pytest.fixture
def study_area():
    polygon = 'POLYGON((-101.744384,39.32155),(-101.552124,39.330048),(-101.403808,39.330048),(-101.332397,39.364032),(-101.744384,39.32155))'

    return StudyArea.objects.create(name='Test study area',
                                    area=polygon)


@pytest.fixture
def study(study_area, agency):
    study = Study.objects.create(title='Test study',
                                 agency=agency)
    study.areas.add(study_area)
    return study


@pytest.fixture
def survey(location, study):
    return Survey.objects.create(study=study,
                                 location=location)


@pytest.mark.django_db
def test_survey_creation(survey):
    pass
