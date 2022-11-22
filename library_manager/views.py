from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from library_manager.models import Book
from library_manager.serializer import PublisherSerializer, BookSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

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


@api_view(['GET'])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        print(books)
        
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False) 

@api_view(['GET'])
def books_list_title(request, title):
    if request.method == 'GET':
        if title is not None:
            books = Book.objects.filter(title=title)
        
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)    # 'safe=False' for objects serialization

@api_view(['POST'])
def post(self, request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(self, request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return Response({"status": "success", "data": "Car Deleted"})


