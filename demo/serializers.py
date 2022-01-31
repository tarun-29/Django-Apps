from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Author, Book, BookNumber, Character

class BookNumberSearializer(serializers.ModelSerializer):
  class Meta:
    model = BookNumber
    fields = ['id', 'isbn_10', 'isbn_13',]

class CharacterSearializer(serializers.ModelSerializer):
  class Meta:
    model = Character
    fields = ['id', 'name',]

class AuthorSearializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'name', 'surname']

class BookSearializer(serializers.ModelSerializer):
  number = BookNumberSearializer(many=False)
  characters = CharacterSearializer(many=True)
  authors = AuthorSearializer(many=True)
  class Meta:
    model = Book
    fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number', 'characters', 'authors']

class BookMiniSearializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id', 'title']
