# Generated by Django 3.0.8 on 2020-09-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0004_auto_20200821_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
