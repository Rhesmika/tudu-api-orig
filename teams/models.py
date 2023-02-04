from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    owner = models.ManyToManyField(User)
    image = models.ImageField(
        upload_to='images/', default='../default_team_mi0sbj.png'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Team"
