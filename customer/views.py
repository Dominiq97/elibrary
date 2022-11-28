from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from administrator.models import Administrator
from customer.models import Customer
from customer.permissions import CustomersPermission
from customer.serializers import CustomerRegisterSerializer, CustomerSerializer
from library_manager.models import Book
from library_manager.serializer import BookSerializer


class Create(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer
    permission_classes = (AllowAny,)


class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)
