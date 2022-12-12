from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.views import APIView
from library_manager.models import Book
from rest_framework.parsers import JSONParser
from library_manager.serializer import PublisherSerializer, BookSerializer, BookRegisterSerializer, BookDocumentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from administrator.permissions import AdministratorsPermission
from customer.permissions import CustomersPermission
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.decorators import action

from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend, SuggesterFilterBackend


from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from library_manager.documents import BookDocument

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


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AdministratorsPermission|CustomersPermission,)
    def get_queryset(self):
        title = self.request.query_params.get("title", None)
        author = self.request.query_params.get("author", None)
        publisher = self.request.query_params.get("publisher", None)
        if title:
            qs = Book.objects.filter(title__icontains=title)
            return qs
        if author:
            qs = Book.objects.filter(author__icontains=author)
            return qs
        if publisher:
            qs = Book.objects.filter(publisher__name__icontains=publisher)
            return qs

        return super().get_queryset()


# Elasticsearch document view
class BookDocumentView(DocumentViewSet):
    document = BookDocument
    serializer_class = BookDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend
    ]

    search_fields = (
        'title',
        'author'
    )

    filter_fields = {
        'publisher': 'publisher.name'
    }

    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        }
    }