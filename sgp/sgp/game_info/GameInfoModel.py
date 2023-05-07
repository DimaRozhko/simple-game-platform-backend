from django.db import models


class GameInfoModel(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    rules = models.TextField()
    history = models.TextField()

    class Meta:
        db_table = 'game_info'
