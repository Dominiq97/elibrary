from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from library_manager.models import Book
from library_manager.serializer import PublisherSerializer

book_id = openapi.Parameter('book_id', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_INTEGER)

FETCH_BOOK_SUCCESS = '''{{
    "id": <publisher id>, 
    "name": <publisher name>,
    "address": <publisher address>,
    "book": [
        {
            "id": <book id>,
            "title": <book name>,
            "publisher": <publisher id>
        }
    ]
}}'''


class LibraryViewset(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer

    def get_queryset(self):
        book_id = self.request.query_params.get('book_id')
        book = Book.objects.get(id=book_id)
        return book.publisher

    @swagger_auto_schema(
        operation_description="give book id to get publisher details",
        manual_parameters=[book_id],
        responses={200: FETCH_BOOK_SUCCESS}

    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PublisherSerializer(queryset)
        return Response(serializer.data)

