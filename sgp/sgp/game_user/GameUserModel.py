from django.db import models


class GameUserModel(models.Model):

    id = models.IntegerField(primary_key=True)
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()
    best_time = models.TextField()
    favorite_game_id = models.IntegerField()
    game_time_id = models.IntegerField()

    class Meta:
        db_table = 'game_user'

