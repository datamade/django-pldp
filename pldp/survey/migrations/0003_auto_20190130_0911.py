# Generated by Django 2.1.3 on 2019-01-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190129_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='representation',
            field=models.CharField(blank=True, choices=[('absolute', 'Absolute'), ('relative', 'Relative')], help_text='Indicate whether the data collected a total of the people present within the survey count time or a representative sample', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='time_start',
            field=models.DateTimeField(blank=True, help_text='Exact date and time that the survey count started', null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='time_stop',
            field=models.DateTimeField(blank=True, help_text='Exact date and time that the survey count stopped. Surveys of moving people should be no less than 10 minutes in length. Surveys of stationary people should be snapshots in time.', null=True),
        ),
    ]
