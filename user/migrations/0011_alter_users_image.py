# Generated by Django 4.0 on 2022-04-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0010_alter_users_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="image",
            field=models.CharField(
                default="https://greendoorhope.s3.amazonaws.com/img/profile_default.png", max_length=256
            ),
        ),
    ]
