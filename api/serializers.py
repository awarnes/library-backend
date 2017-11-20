from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Book, Bookcase, Genre, Reader, Review, Loan

class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reader
        fields = ('url', 'username', 'email', 'friends')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'date_published', 'genre', 'edition')

class BookcaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookcase
        fields = ('reader', 'books')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'description')

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = ('book', 'loaner', 'borrower', 'date_loaned', 'expected_return_date', 'date_returned')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Review
          fields = ('date', 'title', 'reader', 'body', 'stars', 'book', )