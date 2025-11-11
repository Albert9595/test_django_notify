
Сервис для отправки уведомлений пользователям с поддержкой нескольких каналов: Email, SMS, Telegram.  
Если один способ не сработал, задача переходит на следующий канал. Реализована надежная доставка через Celery с ретраями и хранением статусов в базе данных.

Стек:  
 • Python 3.11  
 • Django 4.x  
 • Django REST Framework  
 • PostgreSQL  
 • Celery + Redis  
 • Docker / Docker Compose  

Функциональность  

 • Создание пользователей с контактными данными (email, телефон, telegram_id)  
 • Создание уведомлений через REST API  
 • Ретраи в Celery при ошибках  
 • Хранение статусов и количества попыток отправки  
 • Логирование ошибок  
  
Установка локально (без Docker)  

 1. Клонируем проект:
 2. Создаем виртуальное окружение:
 3. Устанавливаем зависимости:
 4. Создаем файл .env в корне проекта (пример):

DEBUG=True  
SECRET_KEY=your-secret-key  
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1  
DATABASE_URL=postgres://user:password@localhost:5432/dbname  
REDIS_URL=redis://localhost:6379/0  

SMTP_HOST=smtp.example.com  
SMTP_PORT=587  
SMTP_USER=user@example.com  
SMTP_PASSWORD=secret  

TG_BOT_TOKEN=your_telegram_bot_token  
SMS_API_URL=  
SMS_API_KEY=  

 5. Применяем миграции:
 7. Запускаем сервер:
 8. Запускаем Celery worker:

   celery -A notif_project worker --loglevel=info


REST API  

 • Пользователи: /api/users/  
 • GET, POST, PUT, DELETE  
 • Уведомления: /api/notifications/  
 • GET, POST, PUT, DELETE  
 • При создании уведомления автоматически запускается Celery задача отправки  

Пример создания уведомления:  

POST /api/notifications/
{
  "user": 1,
  "message": "Hello from Notification Service"
}
