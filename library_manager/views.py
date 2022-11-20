from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from showroom_manager.models import Book
from showroom_manager.serializer import ShowroomSerializer

book_id = openapi.Parameter('car_id', in_=openapi.IN_QUERY,
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
    serializer_class = ShowroomSerializer

    def get_queryset(self):
        # fetch specific showroom details from car id
        book_id = self.request.query_params.get('book_id')
        book = Book.objects.get(id=book_id)
        return book.showroom

    @swagger_auto_schema(
        operation_description="give car id to get showroom details",
        manual_parameters=[car_id],
        responses={200: FETCH_BOOK_SUCCESS}

    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ShowroomSerializer(queryset)
        return Response(serializer.data)

