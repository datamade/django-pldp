import random
import sys

import pytest

from pldp.models import Survey, SurveyRow, SurveyComponent
from pldp.forms import GENDER_BASIC_CHOICES, AGE_BASIC_CHOICES, \
    AGE_DETAILED_CHOICES, AGE_COMPLEX_CHOICES


@pytest.mark.django_db
def test_survey_row(survey, survey_row, survey_component):
    row = SurveyRow.objects.get(survey_id=survey.id)

    assert survey.row == row


@pytest.mark.django_db
def test_survey_components(survey, survey_row, survey_component):
    assert str(survey.components.first().label) == 'Test label'


@pytest.mark.django_db
@pytest.mark.parametrize('detail_level, response_count', [
    ('detailed', 10,),
])
def test_survey_creation(survey, detail_level, response_count):
    for response in range(response_count):

        total = random.choice(range(100))
        row = SurveyRow.objects.create(survey=survey, total=total)

        choice_level = 'AGE_{}_CHOICES'.format(detail_level.upper())
        choices = getattr(sys.modules[__name__], choice_level)

        age = random.choice(choices)[0]
        name = "Test name"
        label = "Test label"
        type = "Test type"
        position = 1
        saved_data = "Test saved data"

        comp_kwargs = {
                        'detail_level': detail_level,
                        'row': row,
                        'name': name,
                        'label': label,
                        'type': type,
                        'position': position,
                        'saved_data': saved_data
                        }

        comp = SurveyComponent.objects.create(**comp_kwargs)
