from django.db import models
from django.contrib.auth.models import User

class Reader(User):
    friends = models.ManyToManyField('self')

class Book(models.Model):
    title = models.CharField(max_length=10000)
    author = models.CharField(max_length=10000)
    date_published = models.DateField(blank=True)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, blank=True, null=True)
    edition = models.CharField(max_length=10000, blank=True)

class Bookcase(models.Model):
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE)
    books = models.ManyToManyField('Book', blank=True)
    # size = self.get_size()

    # def get_size(self):
    #    return self.books.objects.all().length()

class Review(models.Model):
    STAR_CHOICES = (
      (1, 1),
      (2, 2),
      (3, 3),
      (4, 4),
      (5, 5)
    )
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=10000)
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    stars = models.PositiveSmallIntegerField(choices=STAR_CHOICES)

    book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Loan(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    loaner = models.ForeignKey('Reader', related_name='loaner', on_delete=models.CASCADE)
    borrower = models.ForeignKey('Reader', related_name='borrower', on_delete=models.CASCADE)

    date_loaned = models.DateField(blank=True)
    expected_return_date = models.DateField(blank=True)
    date_returned = models.DateField(blank=True)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
