# Generated by Django 2.0 on 2018-03-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0003_auto_20180322_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='is360video',
            field=models.BooleanField(default=False),
        ),
    ]
