# Generated by Django 3.0.3 on 2020-03-02 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['date', 'time_from'], 'verbose_name_plural': 'Activities'},
        ),
    ]
