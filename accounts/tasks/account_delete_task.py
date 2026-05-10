from celery import shared_task
from accounts.models import CustomUser
from datetime import timedelta
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

@shared_task
def delete_account(phone):
    try:
        user = CustomUser.objects.get(phone=phone)
    except CustomUser.DoesNotExist:
        logger.info({phone: "does not exist"})
        return

    if timezone.now().date() >= user.deletion_requested_at.date() + timedelta(days=29):
        logger.info({phone: "successfully deleted"})
        user.delete()

    return


@shared_task
def get_users():
    numbers = CustomUser.objects.filter(is_active=True, deletion_requested_at__isnull=False).values_list("phone", flat=True)

    for phone in numbers:
        delete_account.delay(phone)





