from django.shortcuts import render
from rest_framework import viewsets
from api.models import (Reader, Loan, Review, Bookcase, Book, Genre)
from api.serializers import (ReaderSerializer, LoanSerializer, ReviewSerializer,
                              BookcaseSerializer, BookSerializer, GenreSerializer)
class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all().order_by('-date_joined')
    serializer_class = ReaderSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by('-date_loaned')
    serializer_class = LoanSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-date')
    serializer_class = ReviewSerializer

class BookcaseViewSet(viewsets.ModelViewSet):
    queryset = Bookcase.objects.all()
    serializer_class = BookcaseSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-title')
    serializer_class = BookSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
