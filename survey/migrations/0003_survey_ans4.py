# Generated by Django 4.0 on 2022-03-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0002_remove_survey_ans4"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="ans4",
            field=models.TextField(null=True),
        ),
    ]
