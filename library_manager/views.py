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
    #     book = Book.objects.get(title = title)
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
def delete(self, request, id=None):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return Response({"status": "success", "data": "Car Deleted"})

# @api_view(['GET'])
# def books_list_publisher(request, publisher):
#     if request.method == 'GET':
#     #     book = Book.objects.get(publisher = publisher)
#         if publisher is not None:
#             books = Book.objects.filter(publisher=int(publisher))
        
#         books_serializer = BookSerializer(books, many=True)
#         return JsonResponse(books_serializer.data, safe=False)    # 'safe=False' for objects serialization


# @api_view(['GET'])
# def books_list_author(request, author):
#     # if request.method == 'GET':
#     #     book = Book.objects.get(author = author)
#     if author is not None:
#         books = Book.objects.filter(author=author)
    
#     books_serializer = BookSerializer(books, many=True)
#     return JsonResponse(books_serializer.data, safe=False) 


# @api_view(['GET'])
# def books_list_publisher(request, publisher):
#     # if request.method == 'GET':
#     #     book = Book.objects.get(title = title)
#     if publisher is not None:
#         books = Book.objects.filter(publisher=publisher)
    
#     books_serializer = BookSerializer(books, many=True)
#     return JsonResponse(books_serializer.data, safe=False) 

# @api_view(['POST'])
# def add_book(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     else:
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])
# def books_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         books_serializer = BookSerializer(books, many=True)
#         return JsonResponse(books_serializer.data, safe=False) 

# class GetBookViewset(viewsets.ModelViewSet):
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         title = self.request.query_params.get('title')
#         book = Book.objects.get(id=title)
#         return book.showroom

#     @swagger_auto_schema(
#         operation_description="give title to get library details",
#         manual_parameters=[title],
#         responses={200: FETCH_BOOK_SUCCESS}
#     )

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = BookSerializer(queryset)
#         return Response(serializer.data)

# def book_detail(request, title):
#     try: 
#         book = Book.objects.get(title=title) 
#     except Book.DoesNotExist: 
#         return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 
#     if request.method == 'GET': 
#         book_serializer = BookSerializer(book) 
#         return JsonResponse(book_serializer.data) 




