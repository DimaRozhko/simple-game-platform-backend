from rest_framework import serializers
from sgp.game_user.GameUserModel import GameUserModel


class GameUserAllSerialization(serializers.ModelSerializer):
    class Meta:
        model = GameUserModel
        fields = '__all__'


class GameUserLogInSerialization(serializers.ModelSerializer):
    class Meta:
        model = GameUserModel
        fields = ['username', 'email', 'password']
