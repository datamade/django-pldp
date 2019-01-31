# Generated by Django 2.1.3 on 2019-01-30 13:02
import uuid

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20190130_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveycomponent',
            name='survey',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
            preserve_default=False,
        ),
    ]
