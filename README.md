
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
 4. Применяем миграции:
 5. Запускаем сервер:
 6. Запускаем Celery worker:

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
