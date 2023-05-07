"""
URL configuration for sgp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sgp.game_info import game_info_view
from sgp.game_time import game_time_view
from sgp.game_user import game_user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('game-time', game_time_view.get_game_time, name='get_game_time'),
    path('game-inf', game_info_view.get_game_inf, name='get_game_inf'),
    path('auth/log-in', game_user_view.auth_log_in, name='auth_log_in'),
    path('auth/sign-up', game_user_view.auth_sign_up, name='auth_sign_up'),
    path('user/info', game_user_view.get_user_inf, name='get_user_inf'),
    path('game-process/start-time', game_time_view.get_start_time, name='get_user_inf')
]
