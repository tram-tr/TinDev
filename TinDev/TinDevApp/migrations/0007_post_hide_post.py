# Generated by Django 4.1.3 on 2022-11-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TinDevApp", "0006_remove_application_job_company_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hide_post",
            field=models.ManyToManyField(
                related_name="hide",
                to="TinDevApp.candidate",
                verbose_name="NotInterested",
            ),
        ),
    ]
