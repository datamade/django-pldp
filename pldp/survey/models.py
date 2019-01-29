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
                                        help_text=_("Official temperature "
                                                    "measured in the survey "
                                                    "location at the time of "
                                                    "the survey count."))
    method = models.CharField(max_length=20,
                              choices=METHOD_CHOICES,
                              help_text=_("Description of the survey count "
                                          "method"))


class SurveyRow(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class ComponentBase(models.Model):
    type_of_choice = models.CharField(max_length=8,
                                      help_text=_('Level of detail expected by '
                                                  'survey component'))
    basic_choice = models.CharField(max_length=255,
                                    null=True,
                                    blank=True)

    detailed_choice = models.CharField(max_length=255,
                                       null=True,
                                       blank=True)

    complex_choice = models.CharField(max_length=255,
                                      null=True,
                                      blank=True)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._meta.get_field('type_of_choice').choices = self.TYPE_CHOICES
        self._meta.get_field('basic_choice').help_text = self.HELP_TEXT
        self._meta.get_field('basic_choice').choice = self.BASIC_CHOICES
        self._meta.get_field('detailed_choice').help_text = self.HELP_TEXT
        self._meta.get_field('detailed_choice').choice = self.DETAILED_CHOICES
        self._meta.get_field('complex_choice').help_text = self.HELP_TEXT
        self._meta.get_field('complex_choice').choice = self.COMPLEX_CHOICES

    @property
    def choice(self):
        return getattr(self, '{}_choice'.format(self.type_of_choice))


class GenderComponent(ComponentBase):
    TYPE_CHOICES = [
        ('basic', _('Basic choices')),
    ]

    BASIC_CHOICES = [
        ('male', _('Male')),
        ('female', _('Female')),
        ('unknown', _('Unknown')),
    ]
    HELP_TEXT = _('Observed or reported gender.')


class AgeComponent(ComponentBase):
    TYPE_CHOICES = [
        ('basic', _('Basic choices')),
        ('detailed', _('Detailed choices')),
        ('complex', _('Complex choices')),
    ]

    BASIC_CHOICES = [
        ('0-14', _('Child')),
        ('15-24', _('Teen or young adult')),
        ('25-64', _('Adult')),
        ('65+', _('Senior')),
    ]
    DETAILED_CHOICES = [
        ('0-4', _('Infant or young child')),
        ('5-14', _('Child')),
        ('15-24', _('Teen or young adult')),
        ('25-44', _('Adult')),
        ('45-64', _('Mature adult')),
        ('65-74', _('Young senior')),
        ('75+', _('Mature senior')),
    ]
    COMPLEX_CHOICES = []


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

    type_of_component = models.CharField(max_length=15,
                                         db_index=True,
                                         choices=COMPONENT_CHOICES,
                                         help_text=_("Type of survey component"),
                                         default='gender')
    gender = models.ForeignKey(GenderComponent,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    age = models.ForeignKey(AgeComponent,
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE)
    row = models.ForeignKey(SurveyRow, on_delete=models.CASCADE)
    total = models.IntegerField(null=True,
                                blank=True,
                                help_text=_("Indicate the number of people "
                                            "counted within the row. This "
                                            "field is not an ID, but it should "
                                            "be included with every survey."))
