from rest_framework import serializers
from be_messages.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user_author', 'user_recipient','message', 'date')

        