from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    image = models.ImageField(default='activate/static/images/profile_pics/default.png',
                              upload_to='activate/static/images/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
