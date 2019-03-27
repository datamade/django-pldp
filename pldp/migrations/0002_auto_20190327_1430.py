# Generated by Django 2.1.5 on 2019-03-27 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pldp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveycomponentactivities',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentactivities',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveycomponentage',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentage',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveycomponentgender',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentgender',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveycomponentgroups',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentgroups',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveycomponentmode',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentmode',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveycomponentobjects',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentobjects',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveycomponentposture',
            name='row',
        ),
        migrations.RemoveField(
            model_name='surveycomponentposture',
            name='survey',
        ),
        migrations.DeleteModel(
            name='SurveyComponentActivities',
        ),
        migrations.DeleteModel(
            name='SurveyComponentAge',
        ),
        migrations.DeleteModel(
            name='SurveyComponentGender',
        ),
        migrations.DeleteModel(
            name='SurveyComponentGroups',
        ),
        migrations.DeleteModel(
            name='SurveyComponentMode',
        ),
        migrations.DeleteModel(
            name='SurveyComponentObjects',
        ),
        migrations.DeleteModel(
            name='SurveyComponentPosture',
        ),
    ]