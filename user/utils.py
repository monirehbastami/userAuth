from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from django.core.mail import EmailMessage
from userauth.settings import EMAIL_HOST_USER
from userauth.celery import app
from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)

@shared_task
def send_reset_password_email_task(email,url):
    email_subject = 'Reset Password Verification'
    email_body = 'Hello ' + email + \
                 '\n Click the following link for reset password \n' + url
    sleep(10)
    send_mail(email_subject,email_body,settings.EMAIL_HOST_USER,[email])
    return None




@shared_task
def send_otp_email(otp_code,receiver):
    email = EmailMessage("otp",f"otp-code: {otp_code}",EMAIL_HOST_USER,[receiver])
    email.send()

def send_confirmation_email(user):
    subject = 'Confirmation Email'
    message = 'Please confirm your email address to activate your account.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)

    user.is_email_confirmed = False  
    user.save()