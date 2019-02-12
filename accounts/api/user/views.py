from django.contrib.auth import get_user_model
from rest_framework import generics

from rest_framework_jwt.settings import api_settings

from .serializers import UserDetailSerializer
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status

User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    # **********************************
    # def get_serializer_context(self):
    #     return {'request': self.request}
    #


class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username")
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
