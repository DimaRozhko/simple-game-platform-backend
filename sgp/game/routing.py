from django.urls import path

from game.consumers import TicTacToeConsumer

ws_tic_tac_toe_urlpatterns = [
    path('ws/game/tic-tac-toe/play/<int:room_code>/', TicTacToeConsumer.as_asgi()),
]
