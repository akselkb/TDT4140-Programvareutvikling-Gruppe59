# Generated by Django 3.0.3 on 2020-03-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['date', 'time_from'], 'verbose_name_plural': 'Activities'},
        ),
        migrations.AddField(
            model_name='activity',
            name='show_email_address',
            field=models.BooleanField(default=False, verbose_name='vis_e-post'),
        ),
    ]
