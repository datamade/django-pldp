import pytest

from django.core.management import call_command

from countries_plus.models import Country
from pldp.models import Agency, Survey, SurveyRow, SurveyComponent, StudyArea, \
    Study, Location, LocationLine


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
def location(agency, country):
    linestring = 'LINESTRING(-101.744384 39.32155, -101.552124 39.330048, -101.403808 39.330048, -101.332397 39.364032)'
    location = Location.objects.create(agency=agency,
                                       country=country,
                                       name_primary='Test location',
                                       geometry=linestring)
    return location

@pytest.fixture
def location_line(location):
    return LocationLine.objects.create(location=location,
                                       date_measured='2018-11-11')


@pytest.fixture
def study_area():
    polygon = 'POLYGON((-101.744384 39.32155, -101.552124 39.330048, -101.403808 39.330048, -101.332397 39.364032, -101.744384 39.32155))'

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
    survey = Survey.objects.create(study=study,
                                   location=location,
                                   form_id=1,
                                   method='analog')

    return survey


@pytest.fixture
def survey_row(survey):
    survey_row = SurveyRow.objects.create(
        total=5,
        survey=survey,
    )

    return survey_row


@pytest.fixture
def survey_component(survey_row):
    survey_component = SurveyComponent.objects.create(
        detail_level='basic',
        name='8e5a7a02-0e39-4a21-b8f9-710728bf7a70',
        label='Test label',
        type='float',
        position=1,
        saved_data=10,
        row=survey_row,
    )

    return survey_component
