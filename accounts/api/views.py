from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .serializers import UserRegisterSerializer

User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return super().get_serializer_context()
        return {"request": self.request}




class AuthAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({"detail": "You are already authenticated"}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        if qs.count():
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request)
                print(user)
                return Response(response, status=201)
        return Response({"detail": " Invalid request"}, status=400)

# class RegisterAPIView(APIView):
#     permission_classes = []
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return Response({"detail": "You are already registeded and authenticatied"}, status=400)
#
#         data = request.data
#         username = data.get("username")
#         email = data.get("email")
#         password = data.get("password")
#         passowrd2 = data.get("password2")
#
#         if password != passowrd2:
#             return Response({"detail": "password must match."})
#         qs = User.objects.filter(
#             Q(username__iexact=username) |
#             Q(email__iexact=username)
#         )
#         if qs.exists():
#             return Response({"detail": "This username or email already exists"}, status=401)
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         # payload = jwt_payload_handler(user)
#         # token = jwt_encode_handler(payload)
#         # response = jwt_response_payload_handler(token, user, request=request)
#         return Response(data={"detail": "Thank you for registering. Please verify your email"}, status=201)
