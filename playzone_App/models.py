from django.db import models


# Create your models here.

class PlayZoneGame(models.Model):

    game_name = models.CharField(max_length=50, null=True,blank=True)
    description = models.TextField(max_length=1000, blank=True)
    url_link = models.URLField(max_length=60, null=True,blank=True)
    game_image = models.ImageField(upload_to='Game_profile/', default=None,null=True, blank=True)

    def __str__(self):
        return self.game_name



