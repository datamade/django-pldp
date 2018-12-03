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
                                                  "survey count started"))
    time_stop = models.DateTimeField(help_text=_("Exact date and time that the "
                                                 "survey count stopped. Surveys of "
                                                 "moving people should be no less "
                                                 "than 10 minutes in length. "
                                                 "Surveys of stationary people "
                                                 "should be snapshots in time."))
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
                                                  "representative sample"))
    microclimate = models.CharField(max_length=255,
                                    null=True,
                                    blank=True,
                                    help_text=_("Perceived weather condition "
                                                "on the specific survey "
                                                "location."))
    temperature_c = models.IntegerField(null=True,
                                        blank=True,
                                        help_text=("Official temperature "
                                                   "measured in the survey "
                                                   "location at the time of "
                                                   "the survey count."))
    method = models.CharField(max_length=20,
                              choices=METHOD_CHOICES,
                              help_text=_("Description of the survey count "
                                          "method"))


class SurveyRow(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class SurveyComponent(models.Model):
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

    name = models.CharField(max_length=15,
                            db_index=True,
                            choices=COMPONENT_CHOICES,
                            help_text=_("Name of the component"))
    row = models.ForeignKey(SurveyRow, on_delete=models.CASCADE)
    total = models.IntegerField(null=True,
                                blank=True,
                                help_text=_("Indicate the number of people "
                                            "counted within the row. This "
                                            "field is not an ID, but it should "
                                            "be included with every survey."))
    content = models.TextField()
