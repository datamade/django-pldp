import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from countries_plus.models import Country

from .agency import Agency


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
    name_primary = models.CharField(max_length=1000,
                                    help_text=_("Official, specific name of "
                                                "the survey location."))
    name_secondary = models.CharField(max_length=1000,
                                      blank=True,
                                      help_text=_("Secondary or specifying "
                                                  "name of the survey "
                                                  "location. Leave blank if "
                                                  "no specification is "
                                                  "necessary."))
    subdivision = models.CharField(max_length=9,
                                   choices=SUBDIVISION_CHOICES,
                                   blank=True,
                                   help_text=_("Indication of whether the "
                                               "location is a subdivision of "
                                               "a single survey location."))
    character = models.CharField(max_length=15,
                                 blank=True,
                                 choices=CHARACTER_CHOICES,
                                 help_text=_("Primary character of the survey "
                                             "location's immediate "
                                             "surroundings."))
    geometry = models.GeometryField(help_text=_("Polygon or line that "
                                                "describes the geometry "
                                                "of the location. Polygons "
                                                "are intended for counts of "
                                                "people staying in an area "
                                                "while lines are intended for"
                                                "counts of people moving "
                                                "across a threshold."))
    type = models.CharField(max_length=4,
                            choices=TYPE_CHOICES,
                            help_text=_("Indication of whether the location "
                                        "is intended for counts of people "
                                        "moving (across a line), or whether "
                                        "it is intended for counts of people "
                                        "staying (within an area)."))

    def __str__(self):
        return self.name_primary


class LocationLine(models.Model):
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE)
    date_measured = models.DateField(help_text=_("Date that the location's "
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
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE)
    date_measured = models.DateField(help_text=_("Date that the location's "
                                                 "attributes were measured."))
    total_sqm = models.FloatField(null=True,
                                  blank=True,
                                  help_text=_("Total area of the space "
                                              "defined by the area geometry."))
    people_sqm = models.FloatField(null=True,
                                   blank=True,
                                   help_text=_("Area of the space defined by "
                                               "the geometry that is "
                                               "inhabitable and assigned for "
                                               "stationary activities."))
    typology = models.CharField(max_length=255,
                                blank=True,
                                help_text=_("Typology of the space defined "
                                            "within the area geometry."))
