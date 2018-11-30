import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from languages_plus.models import Language
from countries_plus.models import Country


class Agency(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=1000,
                            help_text=_("Full name of the agency that is "
                                        "conducting/posting the study."))
    department = models.CharField(max_length=1000,
                                  null=True,
                                  blank=True,
                                  help_text=_("Specific department within the "
                                              "agency that is responsible for "
                                              "the study. Leave blank, if no "
                                              "such specification is necessary."))
    phone = models.CharField(max_length=100,
                             null=True,
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
                                             "agency posting the study. Leave "
                                             "blank, if only British English "
                                             "is used to fill in the study."))
    type = models.CharField(null=True,
                            blank=True,
                            help_text=_("Character of the type of agency that "
                                        "is conducting/posting the study."))


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

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE,
                                help_text=_("Country that the survey location "
                                            "is based within."))
    region = models.CharField(max_length=1000,
                              null=True,
                              blank=True,
                              on_delete=models.CASCADE,
                              help_text=_("State, county, or municipal "
                                          "boundary of the location."))
    city = models.CharField(max_length=1000,
                            null=True,
                            blank=True,
                            help_text=_("Name of the city that the survey "
                                        "location is based within. Leave "
                                        "blank if the survey location is not "
                                        "based within a city."))
    geometry = models.GeometryField(help_text=_("Line or Polygon that "
                                                "describes the geometry of "
                                                "the location."))
    type = models.CharField(max_length=4,
                            choices=(('line', _("line"), ), ('area', _('area'))),
                            null=True,
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
                                      null=True,
                                      blank=True,
                                      help_text=_("Secondary or specifying "
                                                  "name of the survey location. "
                                                  "Leave blank if no "
                                                  "specification is necessary."))
    subdivision = models.CharField()
