from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from sgp import settings
from django.utils import timezone


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "It's test email"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"


@shared_task(bind=True)
def send_mail_message_subject_func(self, mail_subject, message):
    users = get_user_model().objects.all()
    message_decorated = message_decorator(message, settings.EMAIL_HOST_USER)
    for user in users:
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message_decorated,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"


def message_decorator(message, from_email):
    return message + \
        '\n\n_______________________________' + \
        '\nemail sended: ' + timezone.now().strftime("%m/%d/%Y, %H:%M:%S") + \
        '\nbest regards' + \
        '\n' + from_email


@shared_task(bind=True)
def send_mail_func_schedule(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "It's test email (schedule)"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"