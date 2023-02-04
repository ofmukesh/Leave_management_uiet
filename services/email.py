from django.conf import settings
from django.core.mail.message import EmailMessage
Host = settings.EMAIL_HOST_USER


def compose_email(to, subject, body, cc=['']):

    emailMessage = EmailMessage(
        subject=subject,
        body=body,
        from_email=Host,
        to=to,
        cc=cc,
    )
    emailMessage.content_subtype = "html"

    mail = False
    # if not settings.DEBUG:
    mail = emailMessage.send()

    return mail
