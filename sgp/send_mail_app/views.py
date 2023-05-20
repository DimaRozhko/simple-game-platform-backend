from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from rest_framework.decorators import api_view

from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule


@api_view(['POST'])
def send_mail_to_all(request):
    if request.method == 'POST':
        send_mail_func()
        return HttpResponse("Sent")
    return HttpResponse


@api_view(['POST'])
def schedule_mail(request):
    if request.method == 'POST':
        schedule, created = CrontabSchedule.objects.get_or_create(hour=1, minute=23)
        task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func_schedule')
        return HttpResponse("Done")
