from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_manager import views


urlpatterns = [
    path('api/v1/books/', views.BooksList.as_view(), name = "list_books"),
    path('api/v1/books/<str:title>', views.BookDetail.as_view(), name="search_book_after_title"),
    path('api/v1/books/filter/author/<str:author>', views.BookDetailAuthor.as_view(), name="search_book_after_author"),
    path('api/v1/books/filter/publisher/<int:publisher>', views.BookDetailPublisher.as_view(), name="search_book_after_publisher"),
    path('api/v1/books/add_book/', views.BookCreate.as_view(), name='add_book'),
    path('api/v1/books/<int:pk>/', views.BookAdministrator.as_view(), name='update_delete_book'),
]