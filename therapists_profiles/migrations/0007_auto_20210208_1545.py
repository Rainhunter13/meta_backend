# Generated by Django 3.1.6 on 2021-02-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists_profiles', '0006_auto_20210208_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='photo_url',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]