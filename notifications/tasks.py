from celery import shared_task
from .models import Notification
from .services import send_email, send_sms, send_telegram
from django.db import transaction


@shared_task(bind=True, max_retries=5, default_retry_delay=10)
def send_notification_task(self, notif_id):
    try:
        notif = Notification.objects.select_related('user').get(id=notif_id)
    except Notification.DoesNotExist:
        return

    user = notif.user
    notif.attempts += 1
    notif.save(update_fields=['attempts'])

    # Try email
    if user.email:
        ok = send_email(user.email, notif.message)
        if ok:
            notif.status = 'sent'
            notif.save(update_fields=['status'])
            return True
    # fallback to SMS
    if user.phone:
        ok = send_sms(user.phone, notif.message)
        if ok:
            notif.status = 'partial' if notif.attempts > 1 else 'sent'
            notif.save(update_fields=['status'])
            return True
    # fallback to Telegram
    if user.telegram_id:
        ok = send_telegram(user.telegram_id, notif.message)
        if ok:
            notif.status = 'partial' if notif.attempts > 1 else 'sent'
            notif.save(update_fields=['status'])
            return True

    # nothing worked — retry or fail
    notif.last_error = 'no_channel_available_or_send_failed'
    notif.save(update_fields=['last_error'])
    try:
        raise Exception("All channels failed")
    except Exception as exc:
        # Celery will retry up to max_retries
        raise self.retry(exc=exc)