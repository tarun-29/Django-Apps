# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSearializer

# Create your views here.

# class Another(View):

#   books = Book.objects.all()
#   output = ''
#   for book in books:
#     output += f"We have {book.title} book in our database"


#   def get(self, request):
#     return HttpResponse(self.output)


# def first(request):
#   books = Book.objects.all()
#   return render(request, 'first_temp.html', {'books': books})
#   # return HttpResponse('FIRST MESSAGE FROM VIEWS')

class BookViewSet(viewsets.ModelViewSet):
  serializer_class = BookSearializer
  queryset = Book.objects.all()
