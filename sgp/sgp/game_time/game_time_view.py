from sgp.game_time.GameTimeSerialization import GameTimeSerialization
from sgp.game_time.GameTimeModel import GameTimeModel
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_game_time(request):
    if request.method == 'GET':
        result = GameTimeModel.objects.all()
        serialize = GameTimeSerialization(result, many=True)
        return Response(serialize.data)


@api_view(['POST'])
def get_start_time(request):
    if request.method == 'POST':
        id = request.GET['id']
        start_time = request.GET['startTime']
        new_time = GameTimeModel(id=id, start_time=start_time)
        new_time.save()
        result = GameTimeModel.objects.all()
        serialize = GameTimeSerialization(result, many=True)
        return Response(serialize.data[0].get('start_time'))
