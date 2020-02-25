# Generated by Django 3.0.3 on 2020-02-25 14:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_auto_20200225_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='registered_users',
            field=models.ManyToManyField(related_name='events_activity_registered', to=settings.AUTH_USER_MODEL, verbose_name='påmeldte brukere'),
        ),
    ]
