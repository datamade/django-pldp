import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from pldp.models.study import Study
from pldp.models.location import Location


class Study(models.Model):
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
    time_start = models.DateTime(help_text=_("Exact date and time that the "
                                             "survey count started"))
    time_stop = models.DateTime(help_text=_("Exact date and time that the "
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
                                    help_text=_("Perceived whether condition "
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



class ComponentBase(models.Model):

    class Meta:
        abstract = True


class Gender(models.Model):
    pass


class Age(models.Model):
    pass


class Mode(models.Model):
    pass


class Posture(models.Model):
    pass


class Activities(models.Model):
    pass


class Groups(models.Model):
    pass


class Objects(models.Model):
    pass


class GeoTag(models.Model):
    pass
