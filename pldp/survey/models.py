import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from pldp.study.models import Study
from pldp.location.models import Location


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
    time_start = models.DateTimeField(help_text=_("Exact date and time that the "
                                                  "survey count started"),
                                      null=True,
                                      blank=True)
    time_stop = models.DateTimeField(help_text=_("Exact date and time that the "
                                                 "survey count stopped. Surveys of "
                                                 "moving people should be no less "
                                                 "than 10 minutes in length. "
                                                 "Surveys of stationary people "
                                                 "should be snapshots in time."),
                                     null=True,
                                     blank=True)
    time_character = models.CharField(max_length=255,
                                      null=True,
                                      blank=True,
                                      help_text=_("Indicate if anything out of "
                                                  "the ordinary took place at "
                                                  "the specific time of the "
                                                  "survey count string that "
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
                                      null=True,
                                      blank=True)
    microclimate = models.CharField(max_length=255,
                                    null=True,
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
                                            "field is not an ID, but it should "
                                            "be included with every survey."),
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

    type_of_component = models.CharField(max_length=10,
                                         help_text=_('The component that is '
                                                     'actually in use'))

    detail_level = models.CharField(max_length=10,
                                    help_text=_('The level of detail that we '
                                                'expect in the responses'),
                                    choices=DETAIL_CHOICES,
                                    default='basic')

    gender = models.CharField(max_length=10,
                              null=True,
                              blank=True,
                              help_text=_('Observed or reported gender'))

    age = models.CharField(max_length=10,
                           null=True,
                           blank=True,
                           help_text=_('Observed or reported age'))

    row = models.ForeignKey(SurveyRow, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @property
    def choice(self):
        return getattr(self, self.type_of_component)


class SurveyComponent(AbstractSurveyComponent):
    '''
    This class exists to basically make it possible to write some meaningful
    tests (and also in case you don't actually want to override anything). We
    might want to remove this eventually? So that it doesn't create an extra
    table in the database.
    '''
    pass
