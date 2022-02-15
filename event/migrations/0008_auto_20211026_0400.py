# Generated by Django 3.2.8 on 2021-10-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20211026_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='admintouristevent',
            name='publish',
            field=models.CharField(choices=[('Publish', 'Publish'), ('Reject', 'Reject'), ('Accept', 'Accept')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='admintouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='Yes', max_length=100),
        ),
        migrations.AlterField(
            model_name='usertouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='Yes', max_length=100),
        ),
    ]
