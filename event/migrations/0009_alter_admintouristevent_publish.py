# Generated by Django 3.2.8 on 2021-10-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20211026_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
