from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Book

class BookSearializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'description', 'price']