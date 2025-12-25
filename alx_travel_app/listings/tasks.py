from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_success_email(email):
    send_mail(
        subject="Payment Successful",
        message="Your booking is confirmed!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )