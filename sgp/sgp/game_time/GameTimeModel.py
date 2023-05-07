from django.db import models


class GameTimeModel(models.Model):

    id = models.IntegerField(primary_key=True)
    start_time = models.TextField()
    end_time = models.TextField()
    game_time = models.TextField()

    class Meta:
        db_table = 'game_time'
