from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_manager import views
from library_manager import views # LibraryViewset #GetBookViewset#, BookViewset

router = DefaultRouter()
# router1 = DefaultRouter()
# router.register(r'', LibraryViewset, basename='books')
# router1.register(r'', GetBookViewset, basename='books')
# router.register(r'books', BookViewset, basename='book')

urlpatterns = [
    path('api/v1/books/', views.books_list),
    path('api/v1/books/<str:title>', views.books_list_title),
    # path('api/v1/books/<int:id>', views.delete),
    # path('api/v1/books/add', views.post),
    # path('api/v1/books/<str:author>', views.books_list_author),
    # path('api/v1/books/<int:publisher>', views.books_list_publisher),
    # path('api/v1/books/add', views.add_book),
    # path('books/', views.books_list, name="books"),
    # path('books/<str:title>', views.book_detail, name="books"),
    
    # path('api/v1/books/<str:title>', views.book_detail, name="book_detail"),
]