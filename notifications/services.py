import smtplib, os, requests
from django.conf import settings

def send_email(to_email: str, message: str) -> bool:
    # Простая SMTP реализация
    SMTP_HOST = os.getenv('SMTP_HOST')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USER = os.getenv('SMTP_USER')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    try:
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(message)
        msg['Subject'] = 'Notification'
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        s = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
        s.starttls()
        s.login(SMTP_USER, SMTP_PASSWORD)
        s.sendmail(SMTP_USER, [to_email], msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print("Email send error:", e)
        return False

def send_sms(phone: str, message: str) -> bool:
    # Замените на реальный провайдер API: Twilio, MessageBird, etc.
    SMS_API_URL = os.getenv('SMS_API_URL')
    SMS_API_KEY = os.getenv('SMS_API_KEY')
    if not SMS_API_URL:
        return False
    try:
        r = requests.post(SMS_API_URL, json={"to": phone, "text": message, "api_key": SMS_API_KEY}, timeout=10)
        return r.status_code == 200
    except Exception as e:
        print("SMS send error:", e)
        return False

def send_telegram(telegram_id: str, message: str) -> bool:
    TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
    if not TG_BOT_TOKEN or not telegram_id:
        return False
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": telegram_id, "text": message}, timeout=10)
        return r.status_code == 200
    except Exception as e:
        print("TG send error:", e)
        return False