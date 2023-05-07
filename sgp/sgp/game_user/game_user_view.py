from django.http import HttpResponse

from sgp.game_user.GameUserSerialization import GameUserAllSerialization, GameUserLogInSerialization
from sgp.game_user.GameUserModel import GameUserModel
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def auth_log_in(request):
    email = request.GET['email']
    password = request.GET['password']
    if request.method == 'GET' and email is not None and password is not None:
        result = GameUserModel.objects.filter(email=email, password=password)
        serialize = GameUserLogInSerialization(result, many=True)
        if len(serialize.data) > 0:
            return Response(serialize.data)
        else:
            return HttpResponse('Unauthorized', status=401)


@api_view(['POST'])
def auth_sign_up(request):
    if request.method == 'POST':
        request_data = request.data
        new_user = GameUserModel(username=request_data.get('username'),
                                 email=request_data.get('email'),
                                 password=request_data.get('password'))
        new_user.save()
        result = GameUserModel.objects.filter(username=request_data.get('username'),
                                              email=request_data.get('email'),
                                              password=request_data.get('password'))
        serialize = GameUserLogInSerialization(result, many=True)
        return Response(serialize.data)


@api_view(['GET'])
def get_user_inf(request):
    if request.method == 'GET':
        request_data = request.data
        user_result = GameUserModel.objects.filter(email=request_data.get('email'), username=request_data.get('username'))
        user_serialize = GameUserAllSerialization(user_result, many=True).data[0]
        return Response(user_serialize)
