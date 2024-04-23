from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        Email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        Email.send()