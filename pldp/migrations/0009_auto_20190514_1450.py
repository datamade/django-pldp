# Generated by Django 2.1.5 on 2019-05-14 14:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pldp', '0008_auto_20190508_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='primary_name',
            new_name='name_primary',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='secondary_name',
            new_name='name_secondary',
        ),
        migrations.RemoveField(
            model_name='location',
            name='area',
        ),
        migrations.RemoveField(
            model_name='location',
            name='line',
        ),
        migrations.RemoveField(
            model_name='locationarea',
            name='geometry',
        ),
        migrations.RemoveField(
            model_name='locationline',
            name='geometry',
        ),
        migrations.AddField(
            model_name='location',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(default='POLYGON((-101.744384 39.32155, -101.552124 39.330048, -101.403808 39.330048, -101.332397 39.364032, -101.744384 39.32155))', help_text='Polygon or line that describes the geometry of the location. Polygons are intended for counts of people staying in an area while lines are intended forcounts of people moving across a threshold.', srid=4326),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationarea',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pldp.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationline',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pldp.Location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='subdivision',
            field=models.CharField(blank=True, choices=[('north', 'north'), ('northeast', 'northeast'), ('east', 'east'), ('southeast', 'southeast'), ('south', 'south'), ('southwest', 'southwest'), ('west', 'west'), ('northwest', 'northwest'), ('center', 'center')], help_text='Indication of whether the location is a subdivision of a single survey location.', max_length=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('line', 'line'), ('area', 'area')], help_text='Indication of whether the location is intended for counts of people moving (across a line), or whether it is intended for counts of people staying (within an area).', max_length=4),
        ),
        migrations.AlterField(
            model_name='locationarea',
            name='date_measured',
            field=models.DateField(help_text="Date that the location's attributes were measured."),
        ),
        migrations.AlterField(
            model_name='locationarea',
            name='total_sqm',
            field=models.FloatField(blank=True, help_text='Total area of the space defined by the area geometry.', null=True),
        ),
        migrations.AlterField(
            model_name='locationarea',
            name='typology',
            field=models.CharField(blank=True, help_text='Typology of the space defined within the area geometry.', max_length=255),
        ),
        migrations.AlterField(
            model_name='locationline',
            name='date_measured',
            field=models.DateField(help_text="Date that the location's attributes were measured."),
        ),
        migrations.AlterField(
            model_name='study',
            name='end_date',
            field=models.DateField(blank=True, help_text='Date of the last survey taking place within a study.', null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='manager_email',
            field=models.EmailField(blank=True, help_text='Direct email to the person in charge of the study.', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='manager_name',
            field=models.CharField(help_text='Name of the person in charge of the study.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='survey',
            name='method',
            field=models.CharField(choices=[('analog', 'Analog'), ('video', 'Video'), ('motion sensor', 'Motion sensor'), ('pressure sensor', 'Pressure sensor'), ('Wi-Fi signal', 'Wi-Fi signal'), ('GPS', 'GPS'), ('radar', 'Radar'), ('cell tower', 'Cell tower'), ('digital application', 'Digital application'), ('drone', 'Drone'), ('road tubes', 'Road tubes')], help_text='Description of the survey count method.', max_length=20),
        ),
        migrations.AlterField(
            model_name='survey',
            name='representation',
            field=models.CharField(blank=True, choices=[('absolute', 'Absolute'), ('relative', 'Relative')], help_text='Indicate whether the data collected a total of the people present within the survey count time or a representative sample.', max_length=8),
        ),
        migrations.AlterField(
            model_name='survey',
            name='time_start',
            field=models.DateTimeField(blank=True, help_text='Exact date and time that the survey count started.', null=True),
        ),
        migrations.AlterField(
            model_name='surveycomponent',
            name='detail_level',
            field=models.CharField(choices=[('basic', 'Basic choices'), ('detailed', 'Detailed choices'), ('complex', 'Complex choices')], default='basic', help_text='The level of detail that we expect in the responses.', max_length=255),
        ),
        migrations.AlterField(
            model_name='surveycomponent',
            name='label',
            field=models.CharField(help_text='The text of this survey question.', max_length=500),
        ),
        migrations.AlterField(
            model_name='surveycomponent',
            name='name',
            field=models.CharField(help_text='The unique identifier of this survey question.', max_length=500),
        ),
        migrations.AlterField(
            model_name='surveycomponent',
            name='position',
            field=models.IntegerField(help_text='The position of this question in the survey.'),
        ),
        migrations.AlterField(
            model_name='surveycomponent',
            name='saved_data',
            field=models.CharField(blank=True, help_text='The submitted answer(s) to this survey question.', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='surveycomponent',
            name='type',
            field=models.CharField(help_text='The type of this survey question.', max_length=500),
        ),
    ]
