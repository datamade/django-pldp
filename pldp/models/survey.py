import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from .location import Location
from .study import Study

from pldp.forms import SURVEY_METHOD_CHOICES, SURVEY_REPRESENTATION_CHOICES

class Survey(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    form_entry = models.IntegerField(help_text=_("ID number of the form used "
                                                 "to submit this survey.")
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
                                      choices=SURVEY_REPRESENTATION_CHOICES,
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
                              choices=SURVEY_METHOD_CHOICES,
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

class SurveyComponent(models.Model):
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

    name = models.CharField(
        max_length=500,
        help_text=('The unique identifier of this survey question'),
    )

    label = models.CharField(
        max_length=500,
        help_text=('The text of this survey question'),
    )

    type = models.CharField(
        max_length=500,
        help_text=_('The type of this survey question'),
    )

    position = models.IntegerField(
        max_length=500,
        help_text=_('The position of this question in the survey'),
    )

    saved_data = models.CharField(
        max_length=500,
        help_text=_('The submitted answer to this survey question'),
    )

    class Meta:
        abstract = True

    @property
    def choice(self):
        return getattr(self, self.type)
