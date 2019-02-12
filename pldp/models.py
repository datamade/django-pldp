import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from languages_plus.models import Language
from countries_plus.models import Country


# Agency model
class Agency(models.Model):
    TYPE_CHOICES = [
        ('governmental agency'), _('governmental agency')),
        ('municipal agency'), _('municipal agency')),
        ('non profit corporation'), _('non profit corporation')),
        ('business corporation'), _('business corporation')),
        ('community organisation'), _('community organisation')),
        ('educational institute'), _('educational institute')),
        ('private individual'), _('private individual')),
    ]

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=1000,
                            help_text=_("Full name of the agency that is "
                                        "conducting/posting the study."))
    department = models.CharField(max_length=1000,
                                  blank=True,
                                  help_text=_("Specific department within the "
                                              "agency that is responsible for "
                                              "the study. Leave blank, if no "
                                              "such specification is "
                                              "necessary."
                                              ))
    phone = models.CharField(max_length=100,
                             blank=True,
                             help_text=_("Direct single voice telephone "
                                         "number for the specified agency."))
    email = models.EmailField(help_text=_("Single valid email address "
                                          "actively monitored by the agency's "
                                          "reception or inquiry desk."))
    language = models.ForeignKey(Language,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 help_text=_("Main language used by the "
                                             "agency posting the study."))
    type = models.CharField(max_length=255,
                            choices=TYPE_CHOICES,
                            blank=True,
                            help_text=_("Character of the type of agency that "
                                        "is conducting/posting the study."))

    def __str__(self):
        return self.name


# Location models
class LocationLine(models.Model):
    geometry = models.LineStringField(srid=4326)
    date_measured = models.DateField(help_text=_("Date that the location_line "
                                                 "attributes were measured."))
    total_m = models.FloatField(null=True,
                                blank=True,
                                help_text=_("Total width of the street/space "
                                            "that the line geometry "
                                            "intersects."))
    pedestrian_m = models.FloatField(null=True,
                                     blank=True,
                                     help_text=_("Width of the pedestrian "
                                                 "area on the street/space "
                                                 "that the line geometry "
                                                 "intersects."))
    bicycle_m = models.FloatField(null=True,
                                  blank=True,
                                  help_text=_("Width of the bicycle area that "
                                              "the line geometry intersects."))
    vehicular_m = models.FloatField(null=True,
                                    blank=True,
                                    help_text=_("Width of the vehicular area "
                                                "that the line geometry "
                                                "intersects."))
    typology_pedestrian = models.CharField(max_length=255,
                                           blank=True,
                                           help_text=_("Typology of the space "
                                                       "assigned for "
                                                       "pedestrians that the "
                                                       "line geometry "
                                                       "intersects."))
    typology_bicycle = models.CharField(max_length=255,
                                        blank=True,
                                        help_text=_("Typology of the space "
                                                    "assigned for bicycles "
                                                    "that the line geometry "
                                                    "intersects."))
    typology_vehicular = models.CharField(max_length=255,
                                          blank=True,
                                          help_text=_("Typology of the space "
                                                      "assigned for vehicles "
                                                      "that the line geometry "
                                                      "intersects."))


class LocationArea(models.Model):
    geometry = models.PolygonField(srid=4326)
    date_measured = models.DateField(help_text=_("Date that the location_area "
                                                 "attributes were measured."))
    total_sqm = models.FloatField(null=True,
                                  blank=True,
                                  help_text=_("Total area of the space "
                                              "defined by the area geometry"))
    people_sqm = models.FloatField(null=True,
                                   blank=True,
                                   help_text=_("Area of the space defined by "
                                               "the geometry that is "
                                               "inhabitable and assigned for "
                                               "stationary activities."))
    typology = models.CharField(max_length=255,
                                blank=True,
                                help_text=_("Typology of the space defined "
                                            "within the area geometry"))


class Location(models.Model):
    TYPE_CHOICES = [
        ('line', _('line')),
        ('area', _('area')),
    ]
    SUBDIVISION_CHOICES = [
        ('north', _('north')),
        ('northeast', _('northeast')),
        ('east', _('east')),
        ('southeast', _('southeast')),
        ('south', _('south')),
        ('southwest', _('southwest')),
        ('west', _('west')),
        ('northwest', _('northwest')),
        ('center', _('center')),
    ]
    CHARACTER_CHOICES = [
        ('commercial', _("Commercial")),
        ('cbd', _("Central business district")),
        ('civic', _("Civic")),
        ('cultural', _("Cultural")),
        ('educational', _("Educational")),
        ('industrial', _("Industrial")),
        ('infrastructural', _("Infrastructural")),
        ('medical', _("Medical")),
        ('mixed', _("Mixed")),
        ('office', _("Office")),
        ('recreational', _("Recreational")),
        ('residential', _("Residential")),
        ('rural', _("Rural")),
        ('stadium', _("Stadium")),
    ]

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE,
                                help_text=_("Country that the survey location "
                                            "is based within."))
    region = models.CharField(max_length=1000,
                              blank=True,
                              help_text=_("State, county, or municipal "
                                          "boundary of the location."))
    city = models.CharField(max_length=1000,
                            blank=True,
                            help_text=_("Name of the city that the survey "
                                        "location is based within. Leave "
                                        "blank if the survey location is not "
                                        "based within a city."))
    line = models.ForeignKey(LocationLine,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE,
                             help_text=_("Line that describes the geometry "
                                         "of the location"))
    area = models.ForeignKey(LocationArea,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE,
                             help_text=_("Polygon that describes the geometry "
                                         "of the location"))
    type = models.CharField(max_length=4,
                            choices=TYPE_CHOICES,
                            blank=True,
                            help_text=_("Indication of whether the location "
                                        "is intended for counts of people "
                                        "moving (across a line), or whether "
                                        "it is intended for counts of people "
                                        "staying (within an area)."))
    primary_name = models.CharField(max_length=1000,
                                    help_text=_("Official, specific name of "
                                                "the survey location."))
    secondary_name = models.CharField(max_length=1000,
                                      blank=True,
                                      help_text=_("Secondary or specifying "
                                                  "name of the survey "
                                                  "location. Leave blank if "
                                                  "no specification is "
                                                  "necessary."))
    subdivision = models.CharField(max_length=9,
                                   choices=SUBDIVISION_CHOICES,
                                   blank=True,
                                   help_text=_("Line Geometry: indication of "
                                               "whether the line is a "
                                               "subdivision of a single survey"
                                               " location. Area Geometry: "
                                               "indication of whether an area "
                                               "is a subdivision of a single "
                                               "survey location."))
    character = models.CharField(max_length=15,
                                 blank=True,
                                 choices=CHARACTER_CHOICES,
                                 help_text=_("Primary character of the survey "
                                             "location's immediate "
                                             "surroundings."))

    def __str__(self):
        return self.primary_name


# Study models
class StudyArea(models.Model):
    name = models.CharField(max_length=1000,
                            help_text=_("Name of the study area"))
    area = models.GeometryField(srid=4326)

    def __str__(self):
        return self.name


class Study(models.Model):
    SCALE_CHOICES = [
        ('district', _('District')),
        ('city', _('City')),
        ('city center', _('City center')),
        ('neighborhood', _('Neighborhood')),
        ('block scale', _('Block scale')),
        ('single site', _('Single site')),
    ]

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000,
                             blank=True,
                             help_text=_("Title or name of the study as given "
                                         "by the conducting agency."))
    project = models.CharField(max_length=1000,
                               blank=True,
                               help_text=_("Title or name of the project that "
                                           "the study is part of. Leave blank "
                                           "if the study is not linked to any "
                                           "other project."))
    project_phase = models.CharField(max_length=100,
                                     blank=True,
                                     help_text=_("Project phase or stage at "
                                                 "the time of the study. Leave"
                                                 " blank if the study is not "
                                                 "linked ot any other project."
                                                 ))
    start_date = models.DateField(null=True,
                                  blank=True,
                                  help_text=_("Date of the first survey taking"
                                              " place within a study."))
    end_date = models.DateField(null=True,
                                blank=True,
                                help_text=_("The date of the last survey "
                                            "taking place within a study"))
    scale = models.CharField(max_length=12,
                             choices=SCALE_CHOICES,
                             blank=True,
                             help_text=_("Approximate scale of the entire "
                                         "study area, irregardless of the "
                                         "amount of survey locations within "
                                         "that study area."))
    areas = models.ManyToManyField(StudyArea,
                                   help_text=_("Area geometries for surveys "
                                               "bundles together within one "
                                               "larger study. Leave blank if "
                                               "no such sub-division is "
                                               "necessary."))
    manager_name = models.CharField(max_length=1000,
                                    help_text=_("Name of the person in charge "
                                                "of the study"))
    manager_email = models.EmailField(null=True,
                                      blank=True,
                                      help_text=_("Direct email to the person "
                                                  "in charge of the study"))
    protocol_version = models.CharField(max_length=5,
                                        default='1.0',
                                        help_text=_("Version of the Public "
                                                    "Life Data Protocol that "
                                                    "the study is written in."
                                                    ))
    notes = models.TextField(null=True,
                             blank=True,
                             help_text=_("Notes that regard the entirety of "
                                         "the study."))

    def __str__(self):
        return '{} - {}'.format(self.agency.name, self.title)


# Survey models
class Survey(models.Model):
    METHOD_CHOICES = [
        ("analog", _("Analog")),
        ("video", _("Video")),
        ("motion sensor", _("Motion sensor")),
        ("pressure sensor", _("Pressure sensor")),
        ("Wi-Fi signal", _("Wi-Fi signal")),
        ("GPS", _("GPS")),
        ("radar", _("Radar")),
        ("cell tower", _("Cell tower")),
        ("digital application", _("Digital application")),
        ("drone", _("Drone")),
        ("road tubes", _("Road tubes")),
    ]

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    time_start = models.DateTimeField(help_text=_("Exact date and time that "
                                                  "the survey count started"),
                                      null=True,
                                      blank=True)
    time_stop = models.DateTimeField(help_text=_("Exact date and time that "
                                                 "the survey count stopped. "
                                                 "Surveys of moving people "
                                                 "should be no less than 10 "
                                                 "minutes in length. "
                                                 "Surveys of stationary people"
                                                 " should be snapshots in "
                                                 "time."),
                                     null=True,
                                     blank=True)
    time_character = models.CharField(max_length=255,
                                      blank=True,
                                      help_text=_("Indicate if anything out "
                                                  "of the ordinary took place "
                                                  "at the specific time of the"
                                                  " survey count string that "
                                                  "may have impacted the "
                                                  "results."))
    representation = models.CharField(max_length=8,
                                      choices=[('absolute', _("Absolute")),
                                               ('relative', _("Relative"))],
                                      help_text=_("Indicate whether the data "
                                                  "collected a total of the "
                                                  "people present within the "
                                                  "survey count time or a "
                                                  "representative sample"),
                                      blank=True)
    microclimate = models.CharField(max_length=255,
                                    blank=True,
                                    help_text=_("Perceived weather condition "
                                                "on the specific survey "
                                                "location."))
    temperature_c = models.IntegerField(null=True,
                                        blank=True,
                                        help_text=_("Official temperature "
                                                    "measured in the survey "
                                                    "location at the time of "
                                                    "the survey count."))
    method = models.CharField(max_length=20,
                              choices=METHOD_CHOICES,
                              help_text=_("Description of the survey count "
                                          "method"))

    def totals(self, query_filters=[]):

        # Takes in a list of ways you'd like to filter the survey results and
        # returns a count by component, by choice

        pass


class SurveyRow(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    total = models.IntegerField(help_text=_("Indicate the number of people "
                                            "counted within the row. This "
                                            "field is not an ID, but it should"
                                            " be included with every survey."),
                                default=1)

    @property
    def response(self):
        response = {}
        for component in self.surveycomponent_set.all():
            response[component.type_of_component] = component.choice

        return response


class AbstractSurveyComponent(models.Model):

    DETAIL_CHOICES = [
        ('basic', _('Basic choices')),
        ('detailed', _('Detailed choices')),
        ('complex', _('Complex choices')),
    ]

    detail_level = models.CharField(max_length=255,
                                    help_text=_('The level of detail that we '
                                                'expect in the responses'),
                                    choices=DETAIL_CHOICES,
                                    default='basic')

    row = models.ForeignKey(SurveyRow, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @property
    def choice(self):
        return getattr(self, self.type_of_component)


class SurveyComponentGender(AbstractSurveyComponent):
    gender = models.CharField(max_length=255,
                              blank=True,
                              help_text=_('Observed or reported gender'))
    count = models.IntegerField(help_text=_("Count the number of people "
                                            "of the specified gender."
                                            ),
                                default=1)

class SurveyComponentAge(AbstractSurveyComponent):
    age = models.CharField(max_length=255,
                           blank=True,
                           help_text=_('Observed or reported age'))
    count = models.IntegerField(help_text=_("Count the number of people "
                                            "of the specified age."
                                            ),
                                default=1)

class SurveyComponentMode(AbstractSurveyComponent):
    mode = models.CharField(max_length=255,
                           blank=True,
                           help_text=_('Observed or reported mode of '
                                       'transportation'))
    count = models.IntegerField(help_text=_("Count the number of people "
                                            "using the specified mode "
                                            "of transportation."
                                            ),
                                default=1)

class SurveyComponentPosture(AbstractSurveyComponent):
    posture = models.CharField(max_length=255,
                           blank=True,
                           help_text=_('Observed or reported physical posture'))
    count = models.IntegerField(help_text=_("Count the number of people "
                                            "in the specified posture."
                                            ),
                                default=1)


class SurveyComponentGroups(AbstractSurveyComponent):
    group = models.CharField(max_length=255,
                           blank=True,
                           help_text=_('Observed or reported size of group'))
    count = models.IntegerField(help_text=_("Count the number of groups "
                                            "of the specified size."
                                            ),
                                default=1)

class SurveyComponentActivities(AbstractSurveyComponent):
    posture = models.CharField(max_length=255,
                           blank=True,
                           help_text=_('Observed or reported activities'))
    count = models.IntegerField(help_text=_("Count the number of people "
                                            "engaging in the specified "
                                            "activity."),
                                default=1)

class SurveyComponentObjects(AbstractSurveyComponent):
    object = models.CharField(max_length=255,
                           blank=True,
                           help_text=_('Observed or reported objects or '
                                       'animals carried'))
    count = models.IntegerField(help_text=_("Count the number of people "
                                            "carrying the specified "
                                            "object or animal."),
                                default=1)
