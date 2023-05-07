from sgp.game_info.GameInfoSerialization import GameInfoSerializers
from sgp.game_info.GameInfoModel import GameInfoModel
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_game_inf(request):
    if request.method == 'GET':
        request_data = request.data
        result = GameInfoModel.objects.filter(id=request_data.get('id'))
        serialize = GameInfoSerializers(result, many=True)
        return Response(serialize.data)
