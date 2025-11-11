from django.urls import path, include
from rest_framework import routers
from notifications.views import NotificationViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]