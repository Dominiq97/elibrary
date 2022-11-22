from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_manager import views
from library_manager import views # LibraryViewset #GetBookViewset#, BookViewset

router = DefaultRouter()
# router.register(r'', views.LibraryViewset, basename='books')

urlpatterns = [
    path('api/v1/books/', views.books_list),
    path('api/v1/books/<str:title>', views.books_list_title),
]