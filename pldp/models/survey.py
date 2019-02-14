import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from .location import Location
from .study import Study

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
                               help_text=_('Observed or reported physical '
                                           'posture'))
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
