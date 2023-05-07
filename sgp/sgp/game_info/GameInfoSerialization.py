from rest_framework import serializers
from sgp.game_info.GameInfoModel import GameInfoModel


class GameInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameInfoModel
        fields = '__all__'
