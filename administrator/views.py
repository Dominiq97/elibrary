from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.models import Administrator
from administrator.permissions import AdministratorsPermission
from administrator.serializers import AdministratorRegisterSerializer, AdministratorSerializer
from library_manager.models import Book
from library_manager.serializer import BookSerializer


class AdministratorCreate(CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorRegisterSerializer
    permission_classes = (AllowAny,)

# class AdministratorBooksList(ListAPIView):
#     permission_classes = [IsAuthenticated,AdministratorsPermission]
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         administrator = Administrator.objects.get(user=self.request.user)
#         books = Book.objects.filter(administrator=administrator)
#         return books
