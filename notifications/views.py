from rest_framework import viewsets
from .models import Notification, User
from .serializers import NotificationSerializer, UserSerializer
from .tasks import send_notification_task

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        notif = serializer.save()
        send_notification_task.delay(notif.id)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer