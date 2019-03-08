from django.utils.translation import ugettext as _

# This is just a stubbed out module to get the beginnings of how we might want
# to handle form validation together. Originally I had some of this logic in
# the models and it was really not working over there and it seemed like the
# forms might be a better place for it.
#
# The thinking here is that, when a survey component is created, we'll save the
# kind of component and the level of detail that we'll want to capture in the
# responses. The catch is that, sometimes there is only one choice so we'll
# need to make sure that when we are doing the form validation, we are using
# the correct list of choices. The logic for that should live downstream of
# this app. My feeling is that this app should only provide the basic tools for
# storing info about a survey and data collected from a survey and if you want
# to make a tool that makes surveys, you'll need to implement that logic in
# your app.

# Choices for SurveyComponentGender
GENDER_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
]

GENDER_BASIC_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
    ('unknown', _('Unknown')),
]

# Choices for SurveyComponentAge
AGE_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
    ('complex', _('Complex choices')),
]
AGE_BASIC_CHOICES = [
    ('0-14', _('0-14')),
    ('15-24', _('15-24')),
    ('25-64', _('25-64')),
    ('65+', _('65+')),
]
AGE_DETAILED_CHOICES = [
    ('0-4', _('0-4')),
    ('5-14', _('5-14')),
    ('15-24', _('15-24')),
    ('25-44', _('25-44')),
    ('45-64', _('45-64')),
    ('65-74', _('65-74')),
    ('75+', _('75+')),
]
AGE_COMPLEX_CHOICES = [
    ('0-4', _('0-4')),
    ('5-9', _('5-9')),
    ('10-14', _('10-14')),
    ('15-17', _('15-17')),
    ('18-24', _('18-24')),
    ('25-34', _('25-34')),
    ('35-44', _('35-44')),
    ('45-54', _('45-54')),
    ('55-64', _('55-64')),
    ('65-74', _('65-74')),
    ('75+', _('75+')),
]

# Choices for SurveyComponentMode
MODE_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
    ('complex', _('Complex choices')),
]
