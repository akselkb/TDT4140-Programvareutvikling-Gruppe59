# Generated by Django 3.0.3 on 2020-03-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0005_auto_20200302_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ntnui_membership',
            field=models.BooleanField(default=False),
        ),
    ]
