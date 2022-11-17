# Generated by Django 3.2.13 on 2022-11-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TinDevApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_num', models.IntegerField()),
                ('candidate_name', models.CharField(max_length=30)),
                ('candidate_username', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('APLY', 'Applied/Pending'), ('REJT', 'Rejected'), ('ACCT', 'Accepted')], default='APLY', max_length=4)),
            ],
        ),
    ]
