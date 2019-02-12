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


GENDER_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
]

GENDER_BASIC_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
    ('unknown', _('Unknown')),
]
AGE_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
    ('complex', _('Complex choices')),
]

AGE_BASIC_CHOICES = [
    ('0-14', _('Child')),
    ('15-24', _('Teen or young adult')),
    ('25-64', _('Adult')),
    ('65+', _('Senior')),
]
AGE_DETAILED_CHOICES = [
    ('0-4', _('Infant or young child')),
    ('5-14', _('Child')),
    ('15-24', _('Teen or young adult')),
    ('25-44', _('Adult')),
    ('45-64', _('Mature adult')),
    ('65-74', _('Young senior')),
    ('75+', _('Mature senior')),
]
AGE_COMPLEX_CHOICES = [
    ('0-4', _('Infant or toddler')),
    ('5-9', _('Pre-schooler / Early childhood')),
    ('10-14', _('General school / Preadolescence / Late childhood')),
    ('15-17', _('Teens / Adolescence')),
    ('18-24', _('Early adult / Young adult')),
    ('25-34', _('Early adult / Adult')),
    ('35-44', _('Adult')),
    ('45-54', _('Adult / Middle aged / Midlife')),
    ('55-64', _('Mature Adult')),
    ('65-74', _('Young senior / Late adult')),
    ('75+', _('Mature senior')),
]
COMPONENT_CHOICES = [
    ('gender', _('Gender')),
    ('age', _('Age')),
    ('mode', _('Mode')),
    ('posture', _('Posture')),
    ('activities', _('Activities')),
    ('groups', _('Groups')),
    ('objects', _('Objects')),
    ('geotag', _('GeoTag')),
]
