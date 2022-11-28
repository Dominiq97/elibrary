from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.views import APIView
from library_manager.models import Book
from library_manager.serializer import PublisherSerializer, BookSerializer, BookRegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from administrator.permissions import AdministratorsPermission
from customer.permissions import CustomersPermission
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.decorators import action
title = openapi.Parameter('title', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)

FETCH_PUBLISHER_SUCCESS = '''{{
    "name": <publisher name>,
    "address": <publisher address>,
    "book": [
        {
            "title": <book name>,
            "publisher": <publisher id>
        }
    ]
}}'''

FETCH_BOOK_SUCCESS = '''{{
    "title": <book title>,
    "author": <book author>,
}}'''

class BooksList(ListAPIView):
    permission_classes = (AdministratorsPermission|CustomersPermission,)
    serializer_class = BookSerializer
    def get_queryset(self):
        books = Book.objects.all()
        return books

class BookCreate(CreateAPIView):
    permission_classes = [IsAuthenticated, AdministratorsPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, AdministratorsPermission)

class BookDetail(APIView):
    permission_classes = (AdministratorsPermission|CustomersPermission,)
    def get(self, request, title):
        if title is not None:
            book = Book.objects.filter(title=title)
        books_serializer = BookSerializer(book, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    
class BookAdministrator(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, AdministratorsPermission]

    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return Response({"status": "success", "data": "Book Deleted"})
        
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id = pk)
        data = request.data.get('book')
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid():
            book = serializer.save()
        return Response({"success": "Book '{}' is updated".format(book.title)})

class BookDetailAuthor(APIView):
    permission_classes = (AdministratorsPermission|CustomersPermission,)
    def get(self, request, author):
        if author is not None:
            book = Book.objects.filter(author=author)
        books_serializer = BookSerializer(book, many=True)
        return JsonResponse(books_serializer.data, safe=False)

class BookDetailPublisher(APIView):
    permission_classes = (AdministratorsPermission|CustomersPermission,)
    def get(self, request, publisher):
        if publisher is not None:
            book = Book.objects.filter(publisher=publisher)
        books_serializer = BookSerializer(book, many=True)
        return JsonResponse(books_serializer.data, safe=False)
