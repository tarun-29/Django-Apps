from csv import list_dialects
from django.contrib import admin

from demo.models import Author, Book, BookNumber, Character

# Register your models here.
# admin.site.register(Book)
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
  # fields = ["title", "description"]
  list_display = ["title", "description"]
  list_filter = ["published"]
  search_fields = ["title"]

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)