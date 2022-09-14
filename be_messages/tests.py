from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, force_authenticate

from .models import User, Message
from rest_framework import status
from .views import MessageViewSet, IndividualMessageViewSet



# Create your tests here.
class UserTestCase(TestCase):
    """ Test module for User model """

    def setUp(self):
        User.objects.create(username="test")
        User.objects.create(username="test2")

    """ Test for user model """
    def test_user_username(self):
        user = User.objects.get(username="test")
        user_2 = User.objects.get(username="test2")
        self.assertEqual(user.username, "test")
        self.assertEqual(user_2.username, "test2")

class MessageTestCase(TestCase):
    """ Test module for Message model """

    def setUp(self):
        user = User.objects.create(username="test")
        user_2 = User.objects.create(username="test2")
        Message.objects.create(user_author=user, user_recipient=user_2, message="test")
    
    """ Test for message string """
    def test_message_str(self):
        message = Message.objects.get(message="test")
        self.assertEqual(str(message), f"test")
    
    """ Test for message model """
    def test_message_model(self):
        user = User.objects.get(username="test")
        user_2 = User.objects.get(username="test2")
        message = Message.objects.get(message="test")
        self.assertEqual(message.user_author, user)
        self.assertEqual(message.user_recipient, user_2)
        self.assertEqual(message.message, "test")
    
    """ Test for creating a message """
    def test_message_create(self):
        factory = APIRequestFactory()
        user = User.objects.get(username="test")
        user_2 = User.objects.get(username="test2")
        request = factory.post('/messages', {'user_author': user.pk, 'user_recipient': user_2.pk, 'message': 'test'})
        force_authenticate(request, user=user)
        response = MessageViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    """ Testing for bad request in message creation"""
    def test_message_create_error(self):
        factory = RequestFactory()
        user = User.objects.get(username="test")
        user_2 = User.objects.get(username="test2")
        request = factory.post('/messages', {'user_author': user, 'user_recipient': user_2.pk, 'message': 'test'})
        force_authenticate(request, user=user)
        response = MessageViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    """ Test for getting all messages"""
    def test_message_list(self):
        factory = RequestFactory()
        request = factory.get('/messages')
        response = MessageViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class IndividualMessageViewSetTestCase(TestCase):
    """ Test module for IndividualMessageViewSet model """

    def setUp(self):
        user = User.objects.create(username="test")
        user_2 = User.objects.create(username="test2")
        Message.objects.create(user_author=user, user_recipient=user_2, message="test")
    
    """ Test for getting messages between two users """
    def test_individual_message_list(self):
        factory = RequestFactory()
        request = factory.get('/messages/1/2')
        response = IndividualMessageViewSet.as_view({'get': 'list'})(request, sender=1, recipient=2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    """ Test for getting messages between two users with bad request """
    def test_individual_message_list_error(self):
        factory = RequestFactory()
        request = factory.get('/messages/1/2')
        response = IndividualMessageViewSet.as_view({'get': 'list'})(request, sender=1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)