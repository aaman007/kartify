from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from kartify.accounts.api.serializers import UserSerializer

User = get_user_model()


class TestAPIView(APIView):
    """
    A very descriptive doc string and this line is the title
    this line also, it would be concatenated so make it short

    It would help the developers using the api
    to better understand the usage of this
    beautiful test api

    Swagger could be a better choice than making al
    the api docs using POSTMAN
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'status': 'success'})


class UsersLCAPIView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UsersRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
