import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Activity(models.Model):
    """Model for activities. Contains all necessary info for a single activity event."""
    title = models.CharField(max_length=200, verbose_name="tittel")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    # CASCADE: If the user gets deleted, the corresponding activities will also be deleted
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_responsible')

    date = models.DateField(verbose_name="fra dato", default=datetime.date.today, blank=True)
    time_from = models.TimeField(verbose_name="time from", default=timezone.now, blank=True)
    time_to = models.TimeField(verbose_name="time to", default=2, blank=True)

    gear = models.CharField(max_length=200, verbose_name="utstyr", default='')

    max_participants = models.IntegerField(default=0, null=True, verbose_name='maks_deltagere')
    registered_users = models.ManyToManyField(User, blank=True, verbose_name='påmeldte brukere',
                                              related_name='%(app_label)s_%(class)s_registered')


    show_email_address = models.BooleanField(verbose_name="vis_e-post", default=False)
    krever_NTNUI_medlemskap = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['date', 'time_from', 'krever_NTNUI_medlemskap']
