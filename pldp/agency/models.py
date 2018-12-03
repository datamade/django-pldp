import uuid

from django.db import models
from django.utils.translation import ugettext as _

from languages_plus.models import Language


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
    type = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            help_text=_("Character of the type of agency that "
                                        "is conducting/posting the study."))

    def __str__(self):
        return self.name
