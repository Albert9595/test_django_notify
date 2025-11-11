from rest_framework import serializers
from .models import Notification, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'telegram_id']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id','user','message','status','created_at','attempts','last_error']
        read_only_fields = ['status','attempts','last_error','created_at']