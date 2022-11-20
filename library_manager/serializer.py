from rest_framework import serializers

from library_manager.models import Publisher, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Book
        fields = ['id', 'title', 'publisher', 'author']


class PublisherSerializer(serializers.ModelSerializer):
    book = BookSerializer(source='book_set', many=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'book']
