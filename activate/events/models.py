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

    date_from = models.DateTimeField(verbose_name="fra dato")
    date_to = models.DateTimeField(verbose_name="til dato")

    gear = models.CharField(max_length=200, verbose_name="utstyr", default='')

    registered_users = models.ManyToManyField(User, blank=True, verbose_name='påmeldte brukere',
                                              related_name='%(app_label)s_%(class)s_registered')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Activities"
