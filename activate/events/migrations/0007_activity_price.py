# Generated by Django 3.0.3 on 2020-03-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20200311_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True, verbose_name='pris'),
        ),
    ]
