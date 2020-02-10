from django.conf import settings
from django.db import models
from django.utils import timezone

class Activity(models.Model):
    """Model for activities. Contains all necessary info for a single activity event."""
    title = models.CharField(max_length=200, verbose_name="tittel")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #responsible = models.ForeignKey(User, .....)
    date_from = models.DateTimeField(verbose_name="fra dato")
    date_to = models.DateTimeField(verbose_name="til dato")
    #registered_users = models.ManyToManyField(User, blank=True, verbose_name='påmeldte brukere')


    def __str__(self):
        return self.title