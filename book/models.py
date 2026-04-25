from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('technology', 'Technology'),
        ('history', 'History'),
        ('other', 'Other'),
    ]


    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    discription = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    isbn = models.CharField('ISBN',max_length=13, unique=True)
    publication_date = models.DateField()    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
