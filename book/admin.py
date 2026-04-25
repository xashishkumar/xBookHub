from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')

