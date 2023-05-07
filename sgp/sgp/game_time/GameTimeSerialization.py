from rest_framework import serializers
from sgp.game_time.GameTimeModel import GameTimeModel


class GameTimeSerialization(serializers.ModelSerializer):
    class Meta:
        model = GameTimeModel
        fields = '__all__'
