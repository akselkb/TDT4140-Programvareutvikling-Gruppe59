import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F, Count, Case, When, Value, BooleanField
from django.utils import timezone


class ActivityManager(models.Manager):
    """QuerySet manager for Activity class to add non-database fields.

    A @property in the model cannot be used because QuerySets (eg. return
    value from .all()) are directly tied to the database Fields -
    this does not include @property attributes."""

    def get_queryset(self):
        """Overrides the models.Manager method"""
        num_participants = Count('registered_users')
        qs = super(ActivityManager, self).get_queryset().annotate(num_participants=Count('registered_users'))
        qs = qs.annotate(is_full=Case(
            When(max_participants__isnull=True, then=Value(False)),
            When(num_participants__gte=F('max_participants'), then=Value(True)),
            default=Value(False),
            output_field=BooleanField()
        ))
        return qs


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
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=True, verbose_name='pris')

    max_participants = models.IntegerField(default=0, null=True, verbose_name='maks_deltagere')
    registered_users = models.ManyToManyField(User, blank=True, verbose_name='påmeldte brukere',
                                              related_name='%(app_label)s_%(class)s_registered')
    meeting_place = models.CharField(max_length=200, verbose_name="oppmøtested")

    show_email_address = models.BooleanField(verbose_name="vis_e-post", default=False)
    krever_NTNUI_medlemskap = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)  # Is the activity cancelled?

    # Overridden objects manager
    objects = ActivityManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['date', 'time_from', 'krever_NTNUI_medlemskap']
