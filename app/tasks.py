from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


@shared_task
def celery_send_email(subject, message, from_email, recipient_list, **kwrags):
    try:
        send_mail(subject, message, from_email, recipient_list, **kwrags)
        return 'success!'
    except Exception as e:
        logger.error("Mail failed to send: {}".format(e))
