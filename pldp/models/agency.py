import uuid

from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from languages_plus.models import Language

# Agency model
class Agency(models.Model):
    TYPE_CHOICES = [
        ('governmental agency', _('governmental agency')),
        ('municipal agency', _('municipal agency')),
        ('non profit corporation', _('non profit corporation')),
        ('business corporation', _('business corporation')),
        ('community organisation', _('community organisation')),
        ('educational institute', _('educational institute')),
        ('private individual', _('private individual')),
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
