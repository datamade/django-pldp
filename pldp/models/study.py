import uuid

from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.utils.translation import ugettext as _

from .agency import Agency


class StudyArea(models.Model):
    name = models.CharField(max_length=1000,
                            help_text=_("Name of the study area"))
    area = models.PolygonField(help_text=_("Draw boundaries above to create "
                                           "a new study area. Studies can "
                                           "be linked to multiple areas, and "
                                           "a study can be made up of "
                                           "multiple surveys."))

    objects = GeoManager()

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
    agency = models.ForeignKey(Agency,
                               help_text=_("Agency conducting the study."),
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=1000,
                             blank=True,
                             help_text=_("Title or name of the study as "
                                         "given by the conducting agency."))
    project = models.CharField(max_length=1000,
                               blank=True,
                               help_text=_("Title or name of the project "
                                           "that the study is part of. Leave "
                                           "blank if the study is not linked "
                                           "to any other project."))
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
                                help_text=_("Date of the last survey "
                                            "taking place within a study."))
    scale = models.CharField(max_length=12,
                             choices=SCALE_CHOICES,
                             blank=True,
                             help_text=_("Approximate scale of the entire "
                                         "study area, regardless of the "
                                         "number of survey locations within "
                                         "that study area."))
    areas = models.ManyToManyField(StudyArea,
                                   help_text=_("Area geometries for surveys "
                                               "bundled together within one "
                                               "larger study. Leave blank if "
                                               "no such sub-division is "
                                               "necessary."),
                                   blank=True)
    manager_name = models.CharField(max_length=1000,
                                    help_text=_("Name of the person in charge "
                                                "of the study."))
    manager_email = models.EmailField(null=True,
                                      blank=True,
                                      help_text=_("Direct email to the person "
                                                  "in charge of the study."))
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

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} - {}'.format(self.agency.name, self.title)
