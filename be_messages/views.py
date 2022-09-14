from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from .models import Message, User
from .serializers import MessageSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

""" View for all messages 
    GET: Returns all messages within the last 30 days limited to 100 messages
    POST: Creates a new message

    Example:
    {
        "user_author": 1,
        "user_recipient": 2,
        "message": "test"
        "date": "2020-10-10T10:10:10Z"
    }

"""

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        current_date = timezone.now()
        earliest_date = current_date - timedelta(days=30)
        queryset = Message.objects.filter(date__range=(earliest_date, current_date))[:100]
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

""" View for individual messages
    GET: Returns messages from specific user to specific user within the last 30 days limited to 100 messages
 
    Example:
    {
        "user_author": 1,
        "user_recipient": 2,
        "message": "test"
        "date": "2020-10-10T10:10:10Z"
    }

"""

class IndividualMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def list(self, request, sender=None, recipient=None):
        if sender is not None and recipient is not None:
            current_date = timezone.now()
            earliest_date = current_date - timedelta(days=30)
            queryset = Message.objects.filter(user_author_id=sender, user_recipient_id=recipient, date__range=(earliest_date, current_date))[:100]
            serializer = MessageSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    


